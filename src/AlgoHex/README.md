# AlgoHex 项目配置记录

本文档为配置文章 **"Locally Meshable Frame Fields"** 的代码的记录 [[Paper]](https://dl.acm.org/doi/10.1145/3592457) [[Project Page]](https://www.algohex.eu/publications/locally-meshable-frame-fields/) [[Code]](https://github.com/cgg-bern/AlgoHex)

```
@article{liu2023locally,
    title={Locally Meshable Frame Fields},
    author={LIU, HENG and BOMMES, DAVID},
    journal={ACM Trans. Graph},
    volume={42},
    number={4},
    year={2023}
    publisher = {ACM},
    address = {New York, NY, USA},
    doi = {10.1145/3592457}
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 5/4/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 预备步骤

- 该项目依赖于 Gurobi 库，安装步骤可参考 [Gurobi 库配置记录](../Gurobi/)

## 配置步骤

参考 [AlgoHex/README](https://github.com/cgg-bern/AlgoHex/blob/main/README.md)

1. 将项目下载到本地：

    ```
    https://github.com/cgg-bern/AlgoHex.git
    ```

    进入项目目录：

    ```
    cd AlgoHex
    ```

2. 新建存放编译文件的目录：

    ```
    mkdir build
    ```
    并进入：

    ```
    cd build
    ```

3. 使用 CMake 进行 configure：

    ```
    cmake -DGUROBI_HOME=/path/to/gurobi ..
    ```

    这里的 `/path/to/gurobi` 要替换为安装 **Gurobi** 库的目录，如我这里为（具体路径根据实际情况而定）：

    ```
    cmake -DGUROBI_HOME=/home/huangcanjia/gurobi1201/linux64/ ..
    ```

    - :warning: 可能出现错误 `Could not find a package configuration file provided by "GMM" ...`

        没有指定 “FindGMM.cmake” 文件，可以下载 https://github.com/libigl/CoMISo/blob/master/cmake/FindGMM.cmake 文件，并将其放置在 “AlgoHex/cmake/” 目录下即可

        或者暂时将文件 “AlgoHex/cmake/AlgoHexDependencies.cmake” 的 Line 19 `find_package(GMM REQUIRED)` 注释掉，让该项目先把后面需要的 **CoMISo** 库下载完毕，然后将 “AlgoHex/external/CoMISo/cmake/FindGMM.cmake” 文件复制到 “AlgoHex/cmake/” 目录下，并取消前面的注释行为，重新进行 configure

    - :warning: 可能出现错误 `Could NOT find CoinUtils`

        这是因为 **QGP3D** 项目配置过程中找不到 **Gurobi** 库导致的

        在文件 “AlgoHex/external/QGP3D/src/CMakeLists.txt” 的 Line 15 添加：
        
        ```
        set(MC3D_USE_GUROBI ON)
        ```

    - :warning: 可能出现错误 `Cannot specify compile options for target "HexHex" which is not built by this project.`

        可能是该团队将此处使用的提取六面体化方法 **HexEx** 与它们自己的工作 **HexHex** 弄混了，将文件 “external/libHexEx/CMakeLists.txt” 的 Line 137 中的 `HexHex` 改为 `HexEx`，即：

        ```
        target_compile_options(HexEx PUBLIC -msse -mfpmath=sse)
        ```

4. 编译：

    ```
    make
    ```

    - :warning: 可能出现错误 `undefined reference to typeinfo for testing::Test`

        在文件 "AlgoHex/CMakeLists.txt" 的 Line 303-304 之间添加：

        ```
        set(ALGOHEX_BUILD_TESTS OFF)
        ```

## 测试

进入 “AlgoHex/build” 目录，输入：

```
./Build/bin/HexMeshing -i ../demo/HexMeshing/cylinder.ovm -o cylinder_hex.ovm
```

- :warning: 可能出现错误 `Local abort before MPI_INIT completed completed successfully, but am not able to aggregate error messages, and not able to guarantee that all other processes were killed!`

    在 “AlgoHex/build” 目录中输入：

    ```
    cmake -DDISABLE_MPI=TRUE .
    cmake -DGUROBI_HOME=/home/huangcanjia/gurobi1201/linux64/ -DDISABLE_MPI=1 ..
    ```

    然后重新进行编译：

    ```
    make
    cmake --build
    ```

    其他解决方法可以参考 [issue #2](https://github.com/cgg-bern/AlgoHex/issues/2), [issue #3](https://github.com/cgg-bern/AlgoHex/issues/3), [issue #9](https://github.com/cgg-bern/AlgoHex/issues/9)