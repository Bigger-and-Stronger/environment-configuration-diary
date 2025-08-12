# Neural-Pull: Learning Signed Distance Functions from Point Clouds by Learning to Pull Space onto Surfaces 环境配置

*Xiaoyang Yu, 2025-8-9*

### 🐧 Linux
平台：Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-125-generic x86_64)

---

### 配置

这是一篇有关配置文章 "*Neural-Pull: Learning Signed Distance Functions from Point Clouds by Learning to Pull Space onto Surfaces*" 的记录。[论文](https://arxiv.org/abs/2011.13495) | [代码仓库（PyTorch版本）](https://github.com/mabaorui/NeuralPull-Pytorch) | [代码仓库（TensorFlow版本）](https://github.com/mabaorui/NeuralPull)

我这里选择 PyTorch版本，仓库中给出的配置命令中部分使用 conda 安装，在我的环境下会卡住，所以我这里选择全部使用 pip 安装

配置：依次输入以下命令


    $ git clone https://github.com/mabaorui/NeuralPull-Pytorch.git

    $ cd NeuralPull-Pytorch/

    $ conda create -n npull python=3.8
    
    $ conda activate npull
    
    $ pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1+cu113 --index-url https://download.pytorch.org/whl/cu113

    $ pip install tqdm==4.66.3 pyhocon==0.3.57 trimesh==3.23.5 PyMCubes==0.1.2 scipy==1.10.1

---

### 测试

作者提供了测试数据


    $ python run.py --gpu 0 --conf confs/npull.conf --dataname gargoyle --dir gargoyle


