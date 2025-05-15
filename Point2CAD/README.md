# Point2CAD 环境配置

*Xiaoyang Yu, 2025-5-15*

### 🐧 Linux

平台：Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-125-generic x86_64)
Cuda 版本：11.6

---

### 配置

这是一篇有关配置文章 "*Point2CAD: Reverse Engineering CAD Models from 3D Point Clouds*" 的记录。[文章主页](https://www.obukhov.ai/point2cad.html) | [代码仓库](https://github.com/prs-eth/point2cad)

文章作者使用 Docker 配置环境，我这里使用 Conda 配置。依次输入以下命令：


    $ git clone https://github.com/prs-eth/point2cad.git

    $ cd point2cad

    $ conda create --name point2cad python=3.7

    $ conda activate point2cad

    $ pip install torch==1.12.1+cu116 torchvision==0.13.1+cu116 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu116

    $ pip install geomdl

    $ pip install numpy

    $ pip install open3d

    $ pip install pyvista

    $ pip install rtree

    $ pip install scipy

    $ pip install tqdm

    $ pip install trimesh

由于有两个不同版本的 Pymesh ([Reference](https://www.jianshu.com/p/c776aaca8570))：

Pymesh by Takuro Wada，如果我们直接使用pip install pymesh来进行安装，装上的就是这个版本。
Pymesh by Qingnan Zhou，这篇文章用到的版本。下载并安装：


    $ wget https://github.com/PyMesh/PyMesh/releases/download/v0.3/pymesh2-0.3-cp37-cp37m-linux_x86_64.whl

    $ pip install pymesh2-0.3-cp37-cp37m-linux_x86_64.whl

运行前需要将 `main.py` 移动到上一级文件夹中


    $ mv point2cad/main.py main.py

    $ python main.py

我导出了环境文件，可以直接使用环境文件来复现安装环境：


    $ conda env create -f environment.yml