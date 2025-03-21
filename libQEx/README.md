# libQEx 项目配置记录

本文档为配置文章 **"QEx: robust quad mesh extraction"** 的代码的记录 [[Paper]](https://dl.acm.org/doi/10.1145/2508363.2508372) [[Code]](https://github.com/hcebke/libQEx)

```
@article{Ebke:2013:QRQ:2508363.2508372,
    author = {Ebke, Hans-Christian and Bommes, David and Campen, Marcel and Kobbelt, Leif},
    title = {{QE}x: Robust Quad Mesh Extraction},
    journal = {ACM Trans. Graph.},
    issue_date = {November 2013},
    volume = {32},
    number = {6},
    month = nov,
    year = {2013},
    issn = {0730-0301},
    pages = {168:1--168:10},
    articleno = {168},
    numpages = {10},
    url = {http://doi.acm.org/10.1145/2508363.2508372},
    doi = {10.1145/2508363.2508372},
    acmid = {2508372},
    publisher = {ACM},
    address = {New York, NY, USA},
    keywords = {integer-grid maps, quad extraction, quad meshing},
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 19/3/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.5 LTS
- SSH IDE：CLion 2024.3.4

## 配置步骤

1. 将项目下载到本地，在终端中输入：

    ```
    git clone https://github.com/hcebke/libQEx.git
    ```

    并进入该项目目录：

    ```
    cd libQEx
    ```

2. 在该项目根目录处新建目录 `build`，并进入该目录：

    ```
    mkdir build
    cd build
    ```

3. 使用 CMake 进行生成：

    ```
    cmake ..
    ```

    - :warning: 可能出现错误 `Could NOT find OpenMesh (missing: OPENMESH_CORE_LIBRARY`

        需要安装 **OpenMesh** 库，具体可以参考 [OpenMesh 库配置记录](../OpenMesh/)

        :bangbang: 需要注意！！！该项目的部分代码可能无法在最新（11.0 版本以上）的 **OpenMesh** 库上编译，经过测试 **OpenMesh 3.0** 是可以成功编译的，该版本可以在 [openmesh官网](https://www.graphics.rwth-aachen.de/software/openmesh/download/) 找到

4. 进行编译：

    ```
    make
    ```

    - :warning: 可能出现很多关于 **OpenMesh** 的错误

        安装的 **OpenMesh** 库不能是最新版本的，经测试，**OpenMesh 3.0** 是可以成功编译的

# 测试

1. 在 CLion（也可以是其他可以使用 SSH 连接的 IDE）使用 SSH 连接该项目，选择 Release 配置编译 **cmdline_tool**，编译成功后会在目录 “/libQEx/cmake-build-release/demo/cmdline_tool”（具体情况视 IDE 的配置而定） 下出现 **cmdline_tool** 文件，在终端中进入该路径：

    ```
    cd cmake-build-release/demo/cmdline_tool
    ```

2. 在项目中目录 “/libQEx/tests/meshes” 下有许多可供测试的模型，测试模型最好是包含 UV 坐标的 “.obj” 的三角网格文件，可以在终端中输入：

    ```
    ./cmdline_tool ../../../tests/meshes/armadillo_param.obj output.obj
    ```

    执行成功后，会在 **cmdline_tool** 文件目录下生成 **output.obj** 的四边形网格文件