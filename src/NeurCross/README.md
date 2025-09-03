# NeurCross: A Neural Approach to Computing Cross Fields for Quad Mesh Generation 环境配置

*Xiaoyang Yu, 2025-9-2*

### 🐧 Linux

平台：Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-125-generic x86_64)

CUDA: 11.6

---

### 配置

这是一篇有关配置文章 "*NeurCross: A Neural Approach to Computing Cross Fields for Quad Mesh Generation*" 的记录。[论文](https://arxiv.org/pdf/2405.13745) | [代码仓库](https://github.com/QiujieDong/NeurCross?tab=readme-ov-file) | [主页](https://qiujiedong.github.io/publications/NeurCross/)

配置：依次输入以下命令


    $ git clone https://github.com/QiujieDong/NeurCross.git

    $ cd NeurCross/

    $ conda create -n neurcross python=3.7
    
    $ conda activate neurcross
    
    $ pip install torch==1.13.1+cu116 torchvision==0.14.1+cu116 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu116

    $ pip install torchinfo trimesh timm==0.6.13 torch-kmeans scipy

---

### 测试

首先修改 `quad_mesh_args.py`，绝对路径改为相对路径

```python
parser.add_argument('--data_path', type=str, default='../data/doubleTorus/input/doubleTorus.ply', help='path to input dir')
```


    $ cd quad_mesh

    $ python train_quad_mesh.py

---

### 四边网格生成

文中只生成了交叉场，根据网格和交叉场，按如下步骤生成四边网格：（[Reference](https://github.com/QiujieDong/NeurCross/issues/1)）

1. 使用老版本（2.5.0）的 [libigl](https://github.com/libigl/libigl/releases/tag/v2.5.0) 中的 miq 获得参数化
2. 使用 [libQEx](https://github.com/hcebke/libQEx) 从参数化获得四边网格

---

### libigl 安装：

我这里选择安装到 `NeurCross/quad_mesh` 路径下


    $ cd NeurCross/quad_mesh

    $ wget https://github.com/libigl/libigl/archive/refs/tags/v2.5.0.tar.gz

    $ tar -zxvf v2.5.0.tar.gz

    $ cd libigl-2.5.0

    $ mkdir build 
    
    $ cd build

    $ cmake ..

此时会报错：

```bash
file='/home/yuxiaoyang/NeurCross/quad_mesh/libigl-2.5.0/build/_deps/boost-subbuild/boost-populate-prefix/src/boost_1_71_0.tar.bz2'
-- SHA256 hash of
/home/yuxiaoyang/NeurCross/quad_mesh/libigl-2.5.0/build/_deps/boost-subbuild/boost-populate-prefix/src/boost_1_71_0.tar.bz2
does not match expected value
expected: 'd73a8da01e8bf8c7eda40b4c84915071a8c8a0df4a6734537ddde4a8580524ee'
actual: '9c2f4b99bc7ddb95a8babff8ba78a4108aa0951243ea919166a7e2e279825502'
-- Hash mismatch, removing...
CMake Error at boost-subbuild/boost-populate-prefix/src/boost-populate-stamp/download-boost-populate.cmake:159 (message):
Each download failed!
make[2]: *** [CMakeFiles/boost-populate.dir/build.make:92: boost-populate-prefix/src/boost-populate-stamp/boost-populate-download] Error 1
make[1]: *** [CMakeFiles/Makefile2:76: CMakeFiles/boost-populate.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
CMake Error at /usr/share/cmake-3.16/Modules/FetchContent.cmake:915 (message):
Build step for boost failed: 2
Call Stack (most recent call first):
/usr/share/cmake-3.16/Modules/FetchContent.cmake:1006 (__FetchContent_directPopulate)
build/_deps/boost-cmake-src/CMakeLists.txt:19 (FetchContent_Populate)
-- Configuring incomplete, errors occurred!
See also "/home/yuxiaoyang/NeurCross/quad_mesh/libigl-2.5.0/build/CMakeFiles/CMakeOutput.log".
See also "/home/yuxiaoyang/NeurCross/quad_mesh/libigl-2.5.0/build/CMakeFiles/CMakeError.log".
```

下载指定版本的 Boost 后重新编译：


    $ wget -P _deps/boost-subbuild/boost-populate-prefix/src https://archives.boost.io/release/1.71.0/source/boost_1_71_0.tar.bz2

    $ cmake ..

    $ make -j

案例 505 中没有导入交叉场与导出 obj，我添加一些功能，详见 [main.cpp](./main.cpp)

---

### libQEx 安装

参照 [libQEx 项目配置记录](../libQEx)
