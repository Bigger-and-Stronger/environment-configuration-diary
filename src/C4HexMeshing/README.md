# C4HexMeshing 配置记录

本文档为配置文章 “Collapsing Embedded Cell Collapses for Safer Hexahedral Meshing” 的代码的记录 [[code]](https://github.com/HendrikBrueckler/C4HexMeshing)

---

Canjia Huang <<huangcanjia0214@gmail.com>> last update 24/4/2026

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 预备步骤

- 该项目依赖于 **Clp** 库，安装步骤可参考 [COIN_OR Clp 库配置记录](../Clp/)
- 该项目依赖于 **Gurobi** 库，安装步骤可参考 [Gurobi 库配置记录](../Gurobi/)

## 配置步骤

1. 将项目下载到本地，在终端中输入：

    ```
    git clone https://github.com/HendrikBrueckler/C4HexMeshing.git
    ```

    并进入项目目录：
    ```
    cd C4HexMeshing/
    ```

2. 新建存放编译结果的目录并进入：

    ```
    mkdir build && cd build
    ```

3. 使用 CMake 进行 configure，同时设置安装的 Gurobi 库路径（以下路径根据实际进行替换）：
    ```
    cmake -DGUROBI_BASE="/home/huangcanjia/gurobi1301/linux64" ..
    ```

    - :warning: 可能出现错误 `Could NOT find CoinUtils (missing: CoinUtils_LIBRARY CoinUtils_INCLUDE_DIR)`

        - 该问题是由于前面输出的 `QGP3D: Not using gurobi, looking for alternatives.` 无法找到 **Gurobi** 库导致的，**QGP** 库由 `git_submodules` 自动下载配置

            首先需要取消 **QGP** 库的自动更新：注释掉 "C4HexMeshing/extern/CMakeLists.txt" 文件的 Line 4

            然后设置 **QGP3D** 库启用 **Gurobi** 库：修改 "C4HexMeshing/extern/QGP3D/src/CMakeLists.txt" 文件，在 Line 5 添加 `set(QGP3D_USE_GUROBI ON)`

            保存后重新进行 configure

        - 该问题也可能是因为寻找 **Clp** 库时无法找到 **CoinUtils** 导致的

            **CoinUtils** 库由 "cmake/FindCoinUtils.cmake" 进行查找，可以通过临时设置变量（具体路径根据实际情况而定，该路径下需要有 "/include/coin/"）：
            ```
            export CoinUtils_DIR=/home/huangcanjia/coinbrew/dist
            ```

            再重新进行 configure

    - :warning: 可能出现错误 `Could NOT find CLP (missing: CLP_INCLUDE_DIR)`

        类似于解决找不到 **CoinUtils** 库的处理方案，**Clp** 库由 "cmake/FindCLP.cmake" 进行查找，可以通过临时设置环境（具体路径根据实际情况而定，该路径下需要有 "/include/coin/"）：
        ```
        export CLP_DIR=/home/huangcanjia/coinbrew/dist
        ```

4. 编译：
    ```
    make -j
    ```

    编译完毕后，在 "C4HexMeshing/build/Build/bin/" 目录下生成可执行文件 "c4hex_cli"

## 测试

进入编译好的目录 "C4HexMeshing/build/Build/bin/"，依赖项目 **MC3D** 中包含了测试文件

执行：
```
./c4hex_cli --input ../../../extern/QGP3D/extern/MC3D/tests/resources/fandisk_algohex.hexex --output-walls res_wall.hexex --output-igm-file res_igm --output-hex-file res_hex
```