# 1-Lipschitz-Neural-Distance-Fields 环境配置

*Xiaoyang Yu, 2025-3-5*

### 🐧 Linux
平台：Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-125-generic x86_64)

---

### 配置

这是一篇有关配置文章 "**1-Lipschitz Neural Distance Fields**" 的记录。[文章主页](https://gcoiffier.github.io/publications/onelipsdf/) | [代码仓库](https://github.com/GCoiffier/1-Lipschitz-Neural-Distance-Fields)

尽管文章作者给出了依赖库列表，但作者没有说明代码使用的 python 版本。考虑到代码中使用了 python 3.10 引入的 `match` 语句，所以 python 版本要大于等于3.10，我这里选择 python 3.12。

需要提前安装：
- conda (用于管理不同项目的环境)
- cuda (我这里使用 cuda-10.1)

配置：依次输入以下命令

```
git clone https://github.com/GCoiffier/1-Lipschitz-Neural-Distance-Fields.git

cd 1-Lipschitz-Neural-Distance-Fields/

conda create --name 1-lip-sdf python=3.12

conda activate 1-lip-sdf

pip3 install -r requirements.txt

```

---

### 测试

作者提供了多种测试。输入可以是**二维曲线、三维曲线、表面网格、三角形汤、带法向点云**；训练网络的损失函数可以是**hKR损失、距离约束 + Eikonal约束、SALD文章中的损失**；查询可以是**等值线重建、等值面重建、等值点采样、骨架采样**。我只测试了**表面网格 + hkR损失 + 等值面重建**。

数据预处理：我的测试数据保存在 `mesh_gt` 中。输入命令 `python extract_dataset_surface_mesh.py mesh_gt/your_test_mesh.obj ` 后，得到的测试数据保存在 `inputs` 中。

使用 hKR 损失项训练 1-Lipschitz 网络：输入命令 `python train_lip.py chair`，中间结果保存在 `output/your_test_mesh` 中。

等值面重建：输入命令 `python reconstruct_surface.py output/your_test_mesh/model_final.pt -iso 0.0` 提取0等值面。输出结果默认在 `output` 中，也可以通过 `-o path/to/output` 设置输出路径。

```

python extract_dataset_surface_mesh.py mesh_gt/your_test_mesh.obj 

python train_lip.py your_test_mesh

python reconstruct_surface.py output/your_test_mesh/model_final.pt -iso 0.0

```