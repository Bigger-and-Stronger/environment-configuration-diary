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

我导出了环境文件，~可以直接使用环境文件来复现安装环境~，考虑到 Pymesh 是手动安装的依赖库，不建议直接使用环境文件来复现环境：


    $ conda env create -f environment.yml

---

Shi Chen <<shichen2001x@gmail.com>> last update 15/5/2025

- :warning: 直接使用环境文件可能出现以下报错：
  
  `ERROR: No matching distribution found for pymesh2==0.3`

  `ERROR: No matching distribution found for torch==1.12.1+cu116`

  在`environment.yml`中注释掉以下行：

    ```
        #  - pymesh2==0.3
        #  - torch==1.12.1+cu116
        #  - torchaudio==0.12.1+cu116
        #  - torchvision==0.13.1+cu116
    ```
  之后进入环境中：

        $  conda activate point2cad

  手动安装：

        $  pip install torch==1.12.1+cu116 torchvision==0.13.1+cu116 torchaudio==0.12.1 -f https://download.pytorch.org/whl/torch_stable.html

        $  wget https://github.com/PyMesh/PyMesh/releases/download/v0.3/pymesh2-0.3-cp37-cp37m-linux_x86_64.whl

        $  pip install pymesh2-0.3-cp37-cp37m-linux_x86_64.whl

- :warning: 运行 `python main.py` 出现如下报错：

    ```
    Traceback (most recent call last):
    File "/home/chenshi/miniconda3/envs/point2cad/lib/python3.7/concurrent/futures/process.py", line 239, in _process_worker
            r = call_item.fn(*call_item.args, **call_item.kwargs)
    File "/home/chenshi/point2cad/point2cad/fitting_one_surface.py", line 186, in process_one_surface
        return out
        UnboundLocalError: local variable 'out' referenced before assignment
    ```
  这是由于某些版本并不允许返回未初始化的局部变量。在 `fitting_one_surface.py` 文件中，找到函数 `process_one_surface` ，第一行加上 `out = None` 即可。

    ```
    def process_one_surface(label, points, labels, cfg, device):
        out = None
        ... ...
    ```

