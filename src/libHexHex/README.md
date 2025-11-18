# libHexHex 配置文档

本文档为配置文章 “HexHex - Highspeed Extraction of Hexahedral Meshes” 的代码 [[doi]](https://dl.acm.org/doi/abs/10.1145/3730940) [[code]](https://github.com/cgg-bern/libHexHex)

```
@article{10.1145/3730940,
    author = {Kohler, Tobias and Heistermann, Martin and Bommes, David},
    title = {HexHex: Highspeed Extraction of Hexahedral Meshes},
    year = {2025},
    issue_date = {August 2025},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    volume = {44},
    number = {4},
    issn = {0730-0301},
    url = {https://doi.org/10.1145/3730940},
    doi = {10.1145/3730940},
    journal = {ACM Trans. Graph.},
    month = jul,
    articleno = {147},
    numpages = {20},
    keywords = {hexahedral meshing, integer-grid map, optimization}
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 15/8/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤

1. 将项目下载到本地：

    ```
    git clone https://github.com/cgg-bern/libHexHex.git
    ```

    并进入项目目录：

    ```
    cd libHexHex
    ```

2. 新建存放编译结果的目录，并进入该目录：

    ```
    mkdir build && cd build
    ```

3. 使用 CMake 进行 configure：

    ```
    cmake ..
    ```

4. 编译：

    ```
    make -j
    ```

## 测试

编译成功后会在 “libHexHex/build/Build/bin” 目录下生成可执行文件

在目录 “libHexHex/tests/testdata/” 下有着一些测试用的输入 “.hexex” 文件

进入 “libHexHex/build/Build/bin” 目录下，输入：

```
./HexHex -i ../../../tests/testdata/s06u.hexex -o ../../../tests/testdata/s06u_result.mesh
```

运行成功后，会在 “libHexHex/tests/testdata/” 目录下生成 “s06u.mesh“ 结果六面体网格文件（使用 **Gmsh** 打开可能会出错，可以使用 **Geogram** 的可视化工具 **vorparview** 查看）