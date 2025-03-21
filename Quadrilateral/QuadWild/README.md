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
    abstract = {We present a new algorithm for the semi-regular quadrangulation of an input surface, driven by its line features, such as sharp creases. We define a perfectly feature-aligned cross-field and a coarse layout of polygonal-shaped patches where we strictly ensure that all the feature-lines are represented as patch boundaries. To be able to consistently do so, we allow non-quadrilateral patches and T-junctions in the layout; the key is the ability to constrain the layout so that it still admits a globally consistent, T-junction-free, and pure-quad internal tessellation of its patches. This requires the insertion of additional irregular-vertices inside patches, but the regularity of the final-mesh is safeguarded by optimizing for both their number and for their reciprocal alignment. In total, our method guarantees the reproduction of feature-lines by construction, while still producing good quality, isometric, pure-quad, conforming meshes, making it an ideal candidate for CAD models. Moreover, the method is fully automatic, requiring no user intervention, and remarkably reliable, requiring little assumptions on the input mesh, as we demonstrate by batch processing the entire Thingi10K repository, with less than 0.5% of the attempted cases failing to produce a usable mesh.},
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

- 该项目依赖于 Gurobi 库，安装步骤可参考 [Gurobi 库配置记录](../../Other-Libraries/Gurobi/)

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

    其中 `GUROBI_COMPILER` 和 `GUROBI_LIB` 的设置可以参考 “gurobi1201/linux64/lib/” 目录下的文件，如我在该目录下存在文件 “libgurobi_g++8.5.a” 和 “libgurobi120.so”，以此来确定我这里填写的参数

    - （可选）如果希望使用 CoMISo（作者推荐），需要进行安装：

        1. 安装 **blas** 库，如果有 root 权限，可以按照 [quadwild/README-build](https://github.com/nicopietroni/quadwild?tab=readme-ov-file#build) 中执行：

            ```
            apt install libblas-dev
            ```

            如果没有 root 权限，可以参考 [lapack, blas, cblas, lapacke 库配置记录](../../Other-Libraries/LAPACK/) 进行安装

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

3. 新建 "build" 文件夹并进入：

    ```
    mkdir build
    cd build
    ```

4. 使用 **qmake** 进行配置，在终端中输入：

    ```
    qmake ../quadwild/quadwild.pro
    ```

    配置成功后会在当前目录下生成 Makefile 文件

5. 编译，在终端中输入：

    ```
    make -j8
    ```

    编译成功后会在该目录下生成可执行文件 “quadwild”

6. （可选）如果先前配置时选择使用 **CoMISo** 库，则还需要将链接库 “xxx/quadwild/libs/CoMISo/build/Build/lib/CoMISo/libCoMISo.so” 复制到该文件夹中（具体路径依据实际情况而定），执行：

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