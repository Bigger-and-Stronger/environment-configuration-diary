# MATTopo: Topology-preserving Medial Axis Transform with Restricted Power Diagram 环境配置

*Xiaoyang Yu, 2025-11-13*

### 🐧 Linux

平台：Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-125-generic x86_64)

CUDA: 11.6

已预装环境依赖：

    $ apt install zlib1g-dev
    $ sudo apt install mesa-common-dev
    $ sudo apt-get install libcgal-dev

---

### 配置

这是一篇有关配置文章 "*MATTopo: Topology-preserving Medial Axis Transform with Restricted Power Diagram*" 的记录。[论文](https://arxiv.org/abs/2403.18761) | [代码仓库](https://github.com/ningnawang/MATTopo) | [主页](https://ningnawang.github.io/projects/2024_mattopo/)

项目配置：

    $ git clone https://github.com/ningnawang/MATTopo.git
    $ mkdir build
    $ cd build
    $ cmake ..

环境中的CMake版本为3.16.3，报错：

```
CMake Error at extern/libmat/src/inputs/CMakeLists.txt:1 (cmake_minimum_required):
  CMake 3.17 or higher is required.  You are running version 3.16.3

CMake Error at extern/libmat/src/matbase/CMakeLists.txt:1 (cmake_minimum_required):
  CMake 3.17 or higher is required.  You are running version 3.16.3

CMake Error at extern/libmat/src/matfun/CMakeLists.txt:1 (cmake_minimum_required):
  CMake 3.17 or higher is required.  You are running version 3.16.3

CMake Error at extern/libmat/src/matfun_fix/CMakeLists.txt:1 (cmake_minimum_required):
  CMake 3.17 or higher is required.  You are running version 3.16.3

CMake Error at extern/libmat/src/IO/CMakeLists.txt:1 (cmake_minimum_required):
  CMake 3.17 or higher is required.  You are running version 3.16.3

CMake Error at extern/libmat/src/CPU/CMakeLists.txt:1 (cmake_minimum_required):
  CMake 3.17 or higher is required.  You are running version 3.16.3
```

由于没有 root 权限，我把以上 CMakLists 文件中的 CMake 版本修改为 3.16 ，并且在项目目录下的 CMakeLists 添加`set(CMAKE_CUDA_FLAGS "${CMAKE_CUDA_FLAGS} --std=c++17")`
```
################################################################################
cmake_minimum_required(VERSION 3.16 FATAL_ERROR)
set(CMAKE_CUDA_ARCHITECTURES 61 75)
project(MATTOPO LANGUAGES CXX CUDA)

# ###############################################################################
set(EXTERNAL_DIR "${CMAKE_CURRENT_SOURCE_DIR}/extern")
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib")
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin")
set(CMAKE_DEBUG_POSTFIX "d")
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC")
set(CMAKE_CUDA_FLAGS "${CMAKE_CUDA_FLAGS} --std=c++17")
```

最后

    $ make -j4

:warning: 需要额外在当前目录的路径下创建文件夹 `../out/mat`，否则运行后不会产生结果输出。

---

### 其他问题
```

CMake Error at /usr/share/cmake-3.16/Modules/CMakeTestCUDACompiler.cmake:46 (message):
  The CUDA compiler

    "/usr/bin/nvcc"

  is not able to compile a simple test program.
```

修改 CMakeCache.txt 中 CUDA compiler 的路径为当前 cuda 路径，我的是

```c
//CUDA compiler
CMAKE_CUDA_COMPILER:FILEPATH=/usr/local/cuda-11.6/bin/nvcc
```

---

```
/home/yuxiaoyang/MATTopo/extern/libmat/include/common_cxx.h(244): error: namespace "std" has no member "filesystem"

/home/yuxiaoyang/MATTopo/extern/libmat/include/common_cxx.h(247): error: name followed by "::" must be a class or namespace name

/home/yuxiaoyang/MATTopo/extern/libmat/include/common_cxx.h(248): error: name followed by "::" must be a class or namespace name
```

项目目录下的 CMakeLists 添加 `set(CMAKE_CUDA_FLAGS "${CMAKE_CUDA_FLAGS} --std=c++17")`

---

```
Warning: "$Entities" not supported yet.  Ignored.
terminate called after throwing an instance of 'PyMesh::MshLoader::ErrorCode'
Aborted (core dumped)
```

原因：项目只能读入 .msh2 文件，输入可能是 .msh4 的文件，可以通过 gmsh 或 meshio 库转换。


```python
import meshio

mesh = meshio.read("xxx.msh")

meshio.write(
    "xxx.msh2",
    mesh,
    file_format="gmsh22",
    binary=False
)
```
