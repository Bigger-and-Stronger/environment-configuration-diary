from open3d import *
import h5py
import sys
import logging
import json
import os
from shutil import copyfile
import numpy as np
import torch.optim as optim
import torch.utils.data
from torch.autograd import Variable
from torch.optim.lr_scheduler import ReduceLROnPlateau
from src.PointNet import PrimitivesEmbeddingDGCNGn
from matplotlib import pyplot as plt
from src.utils import visualize_uv_maps, visualize_fitted_surface
from src.utils import chamfer_distance
from read_config import Config
from src.utils import fit_surface_sample_points
from src.dataset_segments import Dataset
from torch.utils.data import DataLoader
from src.utils import chamfer_distance
from src.segment_loss import EmbeddingLoss
from src.segment_utils import cluster
import time
from src.segment_loss import (
    EmbeddingLoss,
    primitive_loss,
    evaluate_miou,
)
from src.segment_utils import to_one_hot, SIOU_matched_segments
from src.utils import visualize_point_cloud_from_labels, visualize_point_cloud
from src.dataset import generator_iter
from src.mean_shift import MeanShift
from src.segment_utils import SIOU_matched_segments
from src.residual_utils import Evaluation
import time
from src.primitives import SaveParameters

def guard_mean_shift(embedding, quantile, iterations, kernel_type="gaussian"):
    """
    Sometimes if bandwidth is small, number of cluster can be larger than 50,
    but we would like to keep max clusters 50 as it is the max number in our dataset.
    In that case you increase the quantile to increase the bandwidth to decrease
    the number of clusters.
    """
    ms = MeanShift()
    while True:
        _, center, bandwidth, cluster_ids = ms.mean_shift(
            embedding, 10000, quantile, iterations, kernel_type=kernel_type
        )
        if torch.unique(cluster_ids).shape[0] > 49:
            quantile *= 1.2
        else:
            break
    return center, bandwidth, cluster_ids

# Use only one gpu.
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

config = Config(sys.argv[1])
if_normals = config.normals

userspace = ""
Loss = EmbeddingLoss(margin=1.0)

if config.mode == 0:
    # Just using points for training
    model = PrimitivesEmbeddingDGCNGn(
        embedding=True,
        emb_size=128,
        primitives=True,
        num_primitives=10,
        loss_function=Loss.triplet_loss,
        mode=config.mode,
        num_channels=3,
    )
elif config.mode == 5:
    # Using points and normals for training
    model = PrimitivesEmbeddingDGCNGn(
        embedding=True,
        emb_size=128,
        primitives=True,
        num_primitives=10,
        loss_function=Loss.triplet_loss,
        mode=config.mode,
        num_channels=6,
    )

saveparameters = SaveParameters()

model_bkp = model
model_bkp.l_permute = np.arange(10000)
model = torch.nn.DataParallel(model, device_ids=[0])
model.cuda()

split_dict = {"train": config.num_train, "val": config.num_val, "test": config.num_test}
ms = MeanShift()

os.makedirs(userspace + "logs/results/{}/results/".format(config.pretrain_model_path), exist_ok=True)

# evaluation = Evaluation()
alt_gpu = 0
model.eval()

iterations = 50
quantile = 0.015
model.load_state_dict(
    torch.load(userspace + "logs/pretrained_models/" + config.pretrain_model_path)
    )


test_res = []
test_s_iou = []
test_p_iou = []
test_g_res = []
test_s_res = []
PredictedLabels = []
PredictedPrims = []

# 定义文件夹路径
folder_path = "xyz_file"  
output_folder_path = folder_path

# 获取文件夹中的所有 xyz 文件
xyz_files = [f for f in os.listdir(folder_path) if f.endswith('.xyz')]

print(if_normals)

# 循环读取每个 xyz 文件
for file_name in xyz_files:
    file_path = os.path.join(folder_path, file_name)

    # 读取 xyz 文件，每行有六个值（坐标和法向量）
    data = np.loadtxt(file_path).astype(np.float32)

    # 提取坐标和法向量
    points = data[:, :3]  # 前三列是坐标
    normals = data[:, 3:]  # 后三列是法向量

    # 对坐标进行归一化
    # points = normalize_points(points)

    # 转换为 PyTorch 张量并移动到目标设备
    points = torch.from_numpy(points)[None, :].to(device)
    normals = torch.from_numpy(normals)[None, :].to(device)

    # with torch.autograd.detect_anomaly():
    with torch.no_grad():
        if if_normals:
            input = torch.cat([points, normals], 2)
            embedding, primitives_log_prob, embed_loss = model(
                input.permute(0, 2, 1), torch.zeros_like(points)[:, 0], False
            )
        else:
            embedding, primitives_log_prob, embed_loss = model(
                points.permute(0, 2, 1), torch.zeros_like(points)[:, 0], False
            )
    pred_primitives = torch.max(primitives_log_prob[0], 0)[1].data.cpu().numpy()
    embedding = torch.nn.functional.normalize(embedding[0].T, p=2, dim=1)
    _, _, cluster_ids = guard_mean_shift(
        embedding, quantile, iterations, kernel_type="gaussian"
    )
    weights = to_one_hot(cluster_ids, np.unique(cluster_ids.data.data.cpu().numpy()).shape[
        0])
    cluster_ids = cluster_ids.data.cpu().numpy()
    # 将数据准备好保存
    output_data = np.hstack([points[0].cpu().numpy(),  # 坐标
                            normals[0].cpu().numpy(),  # 法向量
                            cluster_ids[:, None],      # 聚类ID
                            pred_primitives[:, None]]) # 类别ID

    # 保存结果,修改文件名后缀为 .seg
    if if_normals:
        output_file_path = os.path.join(output_folder_path, f"segmented_{file_name.replace('.xyz', '.seg')}")
    else:
        output_file_path = os.path.join(output_folder_path, f"segmented_no_nor_{file_name.replace('.xyz', '.seg')}")
    np.savetxt(output_file_path, output_data, fmt='%.6f')


print("nice !!")

