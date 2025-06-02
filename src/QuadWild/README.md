# QuadWild 项目配置记录

本文档为配置文章 **"Reliable Feature-Line Driven Quad-Remeshing"** 的代码的记录 [[Paper]](https://dl.acm.org/doi/10.1145/3450626.3459941) [[Project Page]](https://www.quadmesh.cloud) [[Code]](https://github.com/nicopietroni/quadwild)

```
@article{10.1145/3450626.3459941,
    author = {Pietroni, Nico and Nuvoli, Stefano and Alderighi, Thomas and Cignoni, Paolo and Tarini, Marco},
    title = {Reliable Feature-Line Driven Quad-Remeshing},
    year = {2021},
    issue_date = {August 2021},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    volume = {40},
    number = {4},
    issn = {0730-0301},
    url = {https://doi.org/10.1145/3450626.3459941},
    doi = {10.1145/3450626.3459941},
    journal = {ACM Trans. Graph.},
    month = {jul},
    articleno = {155},
    numpages = {17},
    keywords = {geometry processing, quad-meshing, modelling}
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 21/3/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 预备步骤

- 该项目依赖于 Gurobi 库，安装步骤可参考 [Gurobi 库配置记录](../Gurobi/)

## 配置步骤

1. 将项目下载到本地，在终端中输入：

    ```
    git clone --recursive https://github.com/nicopietroni/quadwild
    ```

    并进入该项目目录：

    ```
    cd quadwild
    ```

2. 编辑 “quadwild/libs/” 目录下的 **libs.pri** 文件：

    ```
    vim libs/libs.pri
    ```

    并设置其中 **External libraries** 的库的目录，如我这里设置为（具体路径和版本依据实际情况而定）：

    ```
    #External libraries
    BOOST_PATH          = /usr/include/boost/
    GUROBI_PATH         = /home/huangcanjia/gurobi1201/linux64/
    GUROBI_COMPILER     = gurobi_g++8.5
    GUROBI_LIB          = gurobi120
    ```

    其中 `GUROBI_COMPILER` 和 `GUROBI_LIB` 的设置可以参考 **Gurobi** 库的安装目录 “gurobi1201/linux64/lib/” 下的文件，如我在该目录下存在文件 `libgurobi_g++8.5.a` 和 `libgurobi120.so`，以此来确定我这里填写的参数

    - （可选）如果希望使用 CoMISo（作者推荐），需要进行安装：

        1. 安装 **blas** 库，如果有 root 权限，可以按照 [quadwild/README-build](https://github.com/nicopietroni/quadwild?tab=readme-ov-file#build) 中执行：

            ```
            apt install libblas-dev
            ```

            如果没有 root 权限，可以参考 [lapack, blas, cblas, lapacke 库配置记录](../LAPACK/) 进行安装

        2. 执行以下命令：

            ```
            cd libs/CoMISo
            mkdir build
            cd build
            cmake ..
            make
            ```
        
        3. 返回根目录：

            ```
            cd ../../../
            ```
        
        4. 最后该项目生成的可执行文件需要链接 `libCoMISo.so` 文件，经过编译后该文件位于 “xxx/quadwild/libs/CoMISo/build/Build/lib/CoMISo/”（具体路径依据实际情况而定）

        :bangbang: 如果希望不使用 CoMISo，则需要注释掉该文件开头 **CONFIGURATION** 中的 `DEFINES += COMISO_FIELD`:

        ```
        #DEFINES += COMISO_FIELD
        ```

1. 新建 "build" 文件夹并进入：

    ```
    mkdir build
    cd build
    ```

2. 使用 **qmake** 进行配置，在终端中输入：

    ```
    qmake ../quadwild/quadwild.pro
    ```

    配置成功后会在当前目录下生成 Makefile 文件

3. 编译，在终端中输入：

    ```
    make -j8
    ```

    编译成功后会在该目录下生成可执行文件 “quadwild”

4. （可选）如果先前配置时选择使用 **CoMISo** 库，则还需要将链接库 “xxx/quadwild/libs/CoMISo/build/Build/lib/CoMISo/libCoMISo.so” 复制到该文件夹中（具体路径依据实际情况而定），执行：

    ```
    cp ../libs/CoMISo/build/Build/lib/CoMISo/libCoMISo.so .
    ```

## 测试

1. 将测试模型放置在该文件夹内，如我这里使用的测试模型是 [jaw.obj](../QuadWild-Bi-MDF-solver/jaw.obj)

2. 在终端执行（具体模型名称根据实际情况而定）：

    ```
    ./quadwild jaw.obj
    ```

3. 运行结束后会在该目录下生成许多过程文件，其中 “jaw_quadrangulation.obj” 和 “jaw_quadrangulation_smooth.obj” （具体名称根据实际情况而定）为最终结果

 - :star: 如果希望导出四边形化过程的中间结果的话，可以在 “quadwild/libs/quadretopology/quadretopology/quadretopology.cpp” 文件的 Line 35 处添加：

    ```
    #define QUADRETOPOLOGY_DEBUG_SAVE_MESHES
    ```

    并在可执行文件 “quadwild” 所在目录下（即 “quadwild/build”）新建目录 “results”

    修改完后重新编译再使用即可，中间结果会存储在新建的目录 “quadwild/build/results” 中