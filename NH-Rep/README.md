# NH-Rep 环境配置

*Xiaoyang Yu, 2025-3-23*

### 🐧 Linux
平台：Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-125-generic x86_64)

---

### NH-Rep 配置

这是有关配置文章 "*Implicit Conversion of Manifold B-Rep Solids by Neural Halfspace Representation*" 的记录。[文章主页](https://guohaoxiang.github.io/projects/nhrep.html) | [代码仓库](https://github.com/guohaoxiang/NH-Rep)


我这里使用conda安装，使用docker安装请参考：[代码仓库](https://github.com/guohaoxiang/NH-Rep)

:warning: 使用docker安装可能需要自己解决一系列bug。

:warning: 安装时可能遇到的问题请参看**文档末尾**。

需要提前安装：
- conda (用于管理不同项目的环境)
- cuda (我这里使用 cuda-11.6)

首先克隆代码仓库

        $ git clone https://github.com/guohaoxiang/NH-Rep.git

        $ cd NH-Rep


:warning: 虽然代码仓库中提供了环境文件，但由于Conda无法找到 `pytorch==1.2.0=py3.7_cuda10.0.130_cudnn7.6.2_0` 的精确构建版本（可能是因为该构建已从仓库中移除），如果直接创建环境，报错：
```        
Solving environment: failed

ResolvePackageNotFound: 
  - pytorch==1.2.0=py3.7_cuda10.0.130_cudnn7.6.2_0
```
考虑到 1.2.0 版本的 pytorch 可能与 NVIDIA GeForce RTX 3090 之间存在的兼容性问题，我选择的安装流程如下：

        $ conda create --name nhrep python=3.8

        $ conda activate nhrep

        $ conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 pytorch-cuda=11.7 -c pytorch -c nvidia

        $ pip install pyhocon 

        $ pip install GPUtil

        $ pip install trimesh

        $ pip install scipy

        $ pip install plotly

        $ pip install scikit-image==0.17.2

        $ pip install tensorboard

        $ pip install six

我这里给出[环境文件](environment.yml)。考虑到具体环境不同，推荐按上述安装步骤自行调整依赖库的版本来安装。
训练测试数据：

        $ cd code/conversion

        $ python run.py --conf setup.conf --pt ../data/output_data



### Iso-Surfacing 配置
这是这篇文章用到的保尖锐等值面提取工作。以下仅给出我个人的安装流程，具体安装、使用可以参考：[代码仓库](https://github.com/xueyuhanlang/IsoSurfacing)

:warning: 安装时可能遇到的问题请参看**文档末尾**。

首先把 IsoSurfacing 仓库克隆到 `NH-Rep/code/IsoSurfacing` 文件夹下

        $ git clone https://github.com/xueyuhanlang/IsoSurfacing.git

        $ cd IsoSurfacing

然后下载两个依赖库：
- 直接下载就行：
[LibTorch 1.7.1+cu101](https://download.pytorch.org/libtorch/cu110/libtorch-cxx11-abi-shared-with-deps-1.7.1%2Bcu110.zip) 
- 可能需要注册：
[CuDNN 8.0.5+cu101](https://developer.nvidia.com/rdp/cudnn-archive)
下载cuDNN Library for Linux (x86)，可能出现下载压缩文件损坏的情况，建议网络条件较好的时候下载。

下载后

        $ unzip libtorch-cxx11-abi-shared-with-deps-1.7.1+cu110.zip

        $ tar -xzvf cudnn-10.1-linux-x64-v8.0.5.39.tgz

解压后的路径：
```
NH-Rep
|--README.md
|--...
|--code
        |--IsoSurfacing
                |--cuda
                |--libtorch
                |--build.sh
                |--CMakeList.txt
                |--...
        |--...
```

两个文件夹就绪后，把`IsoSurfacing/App/console_pytorch/CMakeLists.txt`和`IsoSurfacing/App/evaluation/CMakeLists.txt`中的绝对路径修改为自己的绝对路径`set(CMAKE_PREFIX_PATH /home/yuxiaoyang/NH-Rep/code/IsoSurfacing/libtorch/share/cmake/Torch)`，然后输入

        $ mkdir build 

        $ sed -i 's/\r$//' build.sh

        $ bash ./build.sh
安装成功。



### 可能出现的一系列问题与解决方法

Q1：
```
runtimeerror: cuda error: cublas_status_execution_failed when calling `cublassgemm( handle, opa, opb, m, n, k, &alpha, a, lda, b, ldb, &beta, c, ldc)`
```
A1：1.2.0 版本的 pytorch 在 NVIDIA GeForce RTX 3090 上存在兼容性问题，使用新版本的 pytorch 可以解决这个问题。

---

Q2：
```
AttributeError: module 'skimage.measure' has no attribute 'marching_cubes_lewiner'
```
A2：安装 scikit-image 库的时候没有加版本约束。新版本的 scikit-image 库中没有这个函数，安装流程中已添加版本约束。

---

Q3：
```
build.sh: line 1: cd: $'build\r': No such file or directory
CMake Error: The source directory "/home/yuxiaoyang/NH-Rep" does not appear to contain CMakeLists.txt.
Specify --help for usage, or press the help button on the CMake GUI.
build.sh: line 3: $'make\r': command not found
```
A3：脚本文件的编码问题。输入以下命令修改编码格式为Unix：

        $ sed -i 's/\r$//' build.sh

---

Q4：
```
CMake Error at App/console_pytorch/CMakeLists.txt:3 (find_package):
  By not providing "FindTorch.cmake" in CMAKE_MODULE_PATH this project has
  asked CMake to find a package configuration file provided by "Torch", but
  CMake did not find one.

  Could not find a package configuration file provided by "Torch" with any of
  the following names:

    TorchConfig.cmake
    torch-config.cmake

  Add the installation prefix of "Torch" to CMAKE_PREFIX_PATH or set
  "Torch_DIR" to a directory containing one of the above files.  If "Torch"
  provides a separate development package or SDK, be sure it has been
  installed.
```
A4：作者的CMakeList使用了绝对路径。把`App/console_pytorch/CMakeLists.txt`和`App/evaluation/CMakeLists.txt`中的绝对路径修改为自己的绝对路径`set(CMAKE_PREFIX_PATH /home/yuxiaoyang/NH-Rep/code/IsoSurfacing/libtorch/share/cmake/Torch)`

---

Q5：
 ```
 -- Build files have been written to: /home/yuxiaoyang/NH-Rep/IsoSurfacing
make: *** No targets specified and no makefile found.  Stop.
```
A5：脚本的编码问题导致 build 的时候把文件生成到了源文件夹中而不是 build 文件夹中。删除源文件夹中的`CMakeCache.txt`、`cmake_install.cmake`、`Makefile`等文件后重新编译即可解决问题。

---

Q6：
```
./ISG_console_pytorch -i ./test/teaser.pt -o outputmesh.ply -v -0.01 -d 8
Segmentation fault (core dumped)     
```
A6：pytorch 版本不兼容。测试模型是 1.2.0 版本导出的结果，使用自己训练出的结果可以解决问题。

---

Q7：对其他模型进行等值面提取，pytorch 报错
```
terminate called after throwing an instance of 'torch::jit::ErrorReport'
terminate called recursively
Aborted (core dumped)
```
A7：可能是因为 pytorch 的版本不匹配。我的解决方法是下载匹配的版本：[LibTorch 1.13.1+cu116](https://download.pytorch.org/libtorch/cu116/libtorch-cxx11-abi-shared-with-deps-1.13.1%2Bcu116.zip)，下载完成后重新编译即可解决问题。


