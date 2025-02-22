
import sys
import logging
import json
import os

from read_config import Config
config = Config(sys.argv[1])
GPU = config.gpu

os.environ['CUDA_VISIBLE_DEVICES'] = GPU

from shutil import copyfile
import numpy as np


from gen_test_vis import COLORS_TYPE, visual_labels

from src.dataset_segments import ori_simple_data

from src.smooth_normal_matrix import hpnet_process




def guard_mean_shift(ms, embedding, quantile, iterations, kernel_type="gaussian"):

        while True:
            _, center, bandwidth, cluster_ids = ms.mean_shift(
                embedding, 10000, quantile, iterations, kernel_type=kernel_type
            )
            if torch.unique(cluster_ids).shape[0] > 49:
                quantile *= 1.2
            else:
                break
        return center, bandwidth, cluster_ids




program_root = os.path.dirname(os.path.abspath(__file__)) + "/"
sys.path.append(program_root + "src")

import torch
from src.SEDNet import SEDNet

from src.segment_loss import EmbeddingLoss
from src.segment_utils import SIOU_matched_segments_usecd, compute_type_miou_abc
from src.segment_utils import to_one_hot, SIOU_matched_segments

from src.mean_shift import MeanShift
from src.segment_utils import SIOU_matched_segments


if __name__ == "__main__":
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # test configs
    HPNet_embed = False # ========================= default True 
    NORMAL_SMOOTH_W = 0.5  # =================== default 0.5
    Concat_TYPE_C6 = False # ====================== default False
    Concat_EDGE_C2 = False # ====================== default False
    INPUT_SIZE = 10000 # =====input pc num, default 10000
    my_knn = 64 # ==== default 64
    use_hpnet_type_iou = False
    drop_out_num = 2000 # ====== type seg rand drop  


    prefix="/data/ytliu/parsenet/" # test dataset path prefix
    starts = 0  # default 0 

    if HPNet_embed:
        print("uisng HPNet embeding way!!!!")

    SAVE_VIZ = not sys.argv[2] == "NoSave"

    # type 结果进行数据增强投票
    MULTI_VOTE = sys.argv[3] == "multi_vote"
    if MULTI_VOTE:
        print("type_multi_vote")


    # type 结果进行数据增强投票
    fold5Drop = sys.argv[4] == "fold5drop"
    if fold5Drop:
        print("type_fold5drop")  # ======= 效果好


    if_normals = config.normals

    Use_MyData = True if config.dataset == "my" else False
    # =============== test dataset config

    if Use_MyData:
        config.num_val = config.num_test = 10 
    else:
        config.num_val = config.num_test = 4163


    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")

    fn = "TEST_SEDNet_{}_{}_{}{}{}{}{}{}_smW{}_in{}_knn{}{}_dropnum{}_Recall".format(
            config.pretrain_model_path.split("/")[-1], 
            "MyData" if Use_MyData else "", 
            "normal0" if config.mode==4 else "", 
            "_multi_vote_2" if MULTI_VOTE else "",
            "_fold5Drop" if fold5Drop else "",
            "_HPNet_embed" if HPNet_embed else "",
            "_ConcatType" if Concat_TYPE_C6 else "",
            "_concatEdge" if Concat_EDGE_C2 else "",
            str(NORMAL_SMOOTH_W),
            str(INPUT_SIZE),
            str(my_knn),
            "_hpnetTypeIoU" if use_hpnet_type_iou else "",
            drop_out_num
        )

    file_handler = logging.FileHandler(
        f"./predictions/logs/{fn}.log", mode="a"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(handler)

    with open(
            "./predictions/config/cfg_{}.json".format(fn), "w"
    ) as file:
        json.dump(vars(config), file)
    source_file = __file__
    destination_file = "./predictions/config/code_{}_{}".format(
        fn, __file__.split("/")[-1]
    )
    copyfile(source_file, destination_file)

    userspace = ""
    Loss = EmbeddingLoss(margin=1.0)

    model = SEDNet(
            embedding=True,
            emb_size=128,
            primitives=True,
            num_primitives=6,
            loss_function=Loss.triplet_loss,
            mode=5,
            num_channels=6,
            combine_label_prim=True,   # early fusion
            edge_module=True,  # add edge cls module
            late_fusion=True,  
            nn_nb=my_knn  # default is 64
        )
    model_inst = SEDNet(
            embedding=True,
            emb_size=128,
            primitives=True,
            num_primitives=6,
            loss_function=Loss.triplet_loss,
            mode=5,
            num_channels=6,
            combine_label_prim=True,   # early fusion
            edge_module=True,  # add edge cls module
            late_fusion=True,    # ======================================
            nn_nb=my_knn  # default is 64
        )

    model = model.cuda( )
    model_inst = model_inst.cuda( )

    split_dict = {"train": config.num_train, "val": config.num_val, "test": config.num_test}
    ms = MeanShift()

    model.eval()
    model_inst.eval()

    iterations = 50
    quantile = 0.015

    state_dict = torch.load(config.pretrain_model_path)
    state_dict = {k[k.find(".")+1:]: state_dict[k] for k in state_dict.keys()} if list(state_dict.keys())[0].startswith("module.") else state_dict
    model.load_state_dict(state_dict)


    state_dict = torch.load(config.pretrain_model_type_path)
    state_dict = {k[k.find(".")+1:]: state_dict[k] for k in state_dict.keys()} if list(state_dict.keys())[0].startswith("module.") else state_dict
    model_inst.load_state_dict(state_dict)

    # 定义文件夹路径
    folder_path = "xyz_part_file"  
    output_folder_path = folder_path

    # 获取文件夹中的所有 xyz 文件
    xyz_files = [f for f in os.listdir(folder_path) if f.endswith('.xyz')]

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

        with torch.no_grad():
            if if_normals:
                _input = torch.cat([points, normals], 2)
                primitives_log_prob = model(
                    _input.permute(0, 2, 1), None, False
                )[1]
                embedding, _, _, edges_pred = model_inst(
                    _input.permute(0, 2, 1), None, False
                )           
            else:
                primitives_log_prob = model(
                    points.permute(0, 2, 1), None, False
                )[1]
                embedding, _, _, edges_pred = model_inst(
                    points.permute(0, 2, 1), None, False
                )

            if MULTI_VOTE and not fold5Drop:
                points_big = points * 1.15
                if if_normals:
                    input = torch.cat([points_big, normals], 2)
                    embedding_big, primitives_log_prob_big = model(
                        input.permute(0, 2, 1), None, False
                    )[:2]
                else:
                    embedding_big, primitives_log_prob_big = model(
                        points_big.permute(0, 2, 1), None, False
                    )[:2]

                points_small = points * 0.85
                if if_normals:
                    input = torch.cat([points_small, normals], 2)
                    embedding_small, primitives_log_prob_small = model(
                        input.permute(0, 2, 1), None, False
                    )[:2]
                else:
                    embedding_small, primitives_log_prob_small = model(
                        points_small.permute(0, 2, 1), None, False
                    )[:2]              

                primitives_log_prob = (primitives_log_prob + primitives_log_prob_big + primitives_log_prob_small) / 3


            if fold5Drop and not MULTI_VOTE:
                # batch_points = None
                # batch_normals = None
                total_type_pred = torch.zeros_like(primitives_log_prob).flatten()
                primitives_log_prob_batch = None
                iter_times = 10000 // drop_out_num
                for i in range(iter_times):
                    index = torch.ones(points.shape, dtype=torch.bool).cuda()
                    index[:, i*drop_out_num:(i+1)*drop_out_num, :] = False
                    points_drop = points[index].reshape((1, 10000 - drop_out_num, 3))
                    normals_drop = normals[index].reshape((1, 10000 - drop_out_num, 3))
                    batch_points = points_drop
                    batch_normals = normals_drop
                    
                    if primitives_log_prob_batch is None:
                        if if_normals:
                            input = torch.cat([batch_points, batch_normals], 2)
                            primitives_log_prob_batch = model(
                                    input.permute(0, 2, 1), None, False
                                )[1]
                        else:
                            primitives_log_prob_batch = model(
                                    batch_points.permute(0, 2, 1), None, False
                                )[1]  
                    else:
                        if if_normals:
                            input = torch.cat([batch_points, batch_normals], 2)
                            primitives_log_prob_batch = torch.cat([primitives_log_prob_batch, model(
                                    input.permute(0, 2, 1), None, False
                                )[1]], dim=0)
                        else:
                            primitives_log_prob_batch = torch.cat([primitives_log_prob_batch, model(
                                    batch_points.permute(0, 2, 1), None, False
                                )[1]], dim=0)                     

                for i in range(iter_times):
                    index = torch.ones(primitives_log_prob.shape, dtype=torch.bool).cuda()
                    index[:, :, i*drop_out_num:(i+1)*drop_out_num] = False    
                    total_type_pred[index.flatten()] += primitives_log_prob_batch[i].flatten()

                primitives_log_prob += total_type_pred.reshape(primitives_log_prob.shape)


            if fold5Drop and MULTI_VOTE:
                """
                data augmentation

                """
                angles = [
                    torch.from_numpy(np.array(      
                        [[1, 0, 0],
                        [0, 1, 0],
                        [0, 0, 1]], dtype=np.float32)).cuda( ).unsqueeze(0), 
                    torch.from_numpy(np.array(      
                        [[-1, 0, 0],
                        [0, 1, 0],
                        [0, 0, -1]], dtype=np.float32)).cuda( ).unsqueeze(0),                 
                ] 

                primitives_prob_total = None
                for R in angles:
                    normals_cur = torch.bmm(normals, R)
                    points_cur = torch.bmm(points, R)

                    if if_normals:
                        input = torch.cat([points_cur, normals_cur], 2)
                        primitives_log_prob_cur= model(input.permute(0, 2, 1), None, False)[1]
                    else:
                        primitives_log_prob_cur= model(points_cur.permute(0, 2, 1), None, False)[1]                

                    total_type_pred = torch.zeros_like(primitives_log_prob_cur).flatten()  # 6 x 1w
                    for i in range(5):
                        index = torch.ones(points.shape, dtype=torch.bool, device=torch.device("cuda"))
                        index[:, i*2000:(i+1)*2000, :] = False
                        points_drop = points_cur[index].reshape((1, 8000, 3))
                        normals_drop = normals_cur[index].reshape((1, 8000, 3))  # =========

                    
                        if if_normals:
                            _input = torch.cat([points_drop, normals_drop], 2)
                            primitives_log_prob_batch = model(
                                    _input.permute(0, 2, 1), None, False
                                )[1]
                        else:
                            primitives_log_prob_batch = model(
                                    batch_points.permute(0, 2, 1), None, False
                                )[1] 
                        index = torch.ones(primitives_log_prob_cur.shape, dtype=torch.bool, device=torch.device("cuda"))
                        index[:, :, i*2000:(i+1)*2000] = False    
                        total_type_pred[index.flatten() ] += primitives_log_prob_batch.flatten()

                    primitives_log_prob_cur += total_type_pred.reshape(primitives_log_prob.shape)     

                    if primitives_prob_total is None:
                        primitives_prob_total =  primitives_log_prob_cur
                    else:
                        primitives_prob_total += primitives_log_prob_cur

                primitives_log_prob = primitives_prob_total     


        pred_primitives = torch.max(primitives_log_prob[0], 0)[1].data.cpu().numpy()

        primitives_prob_total = None
        index = None
        total_type_pred = None
    
        if HPNet_embed:
            embedding = hpnet_process(embedding.transpose(1, 2), points, normals, id=val_b_id, 
                types=primitives_log_prob.transpose(1, 2) if Concat_TYPE_C6 else None,
                edges=edges_pred.transpose(1, 2) if Concat_EDGE_C2 else None,
                normal_smooth_w=NORMAL_SMOOTH_W, CHUNK=1000
            )
            embedding = torch.nn.functional.normalize(embedding[0], p=2, dim=1)

        else:
            embedding = torch.nn.functional.normalize(embedding[0].T, p=2, dim=1)

        _, _, cluster_ids = guard_mean_shift(
                ms, embedding, quantile, iterations, kernel_type="gaussian"
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
        output_file_path = os.path.join(output_folder_path, f"segmented_{file_name.replace('.xyz', '.seg')}")
        np.savetxt(output_file_path, output_data, fmt='%.6f')


    print("nice !!")
