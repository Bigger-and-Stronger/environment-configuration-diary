# MC3D 项目配置记录

本文档为配置 “The 3D Motorcycle Complex for Structured Volume Decomposition” 的代码的记录 [[code]](https://github.com/HendrikBrueckler/MC3D)

---

Canjia Huang <<huangcanjia0214@gmail.com>> last update 28/3/2026

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤

1. 将项目下载到本地，在终端中输入：

    ```
    git clone https://github.com/HendrikBrueckler/MC3D.git
    ```

    进入项目目录：

    ```
    cd MC3D
    ```

2. 新建存放编译结果的目录并进入

    ```
    mkdir build && cd build
    ```

3. 使用 CMake 进行 configure，同时选择配置命令行工具、开启单元测试、选择输出：

    ```
    cmake -DMC3D_BUILD_CLI=ON -DMC3D_BUILD_TESTS=ON -DMC3D_ENABLE_LOGGING=ON ..
    ```

    - :warning: 可能出现错误 `fatal: repository 'https://github.com/HendrikBrueckler/volumeshOS-prv.git/' not found`

        该库似乎已被移除，且似乎仅用于可视化，可按照以下方式移除该子模块：

        ```
        cd ..
        git rm --cached extern/volumeshos -f
        git submodule sync
        rm -rf .git/modules/extern/volumeshos
        cd build
        ```

        再重新进行 configure 步骤

4. 编译：

    ```
    make -j
    ```

    编译成功后在根目录下的 `build/Build/bin/` 目录下生成可执行文件 `mc3d_cli`


## 测试

于项目根目录下的 `tests/resouces/` 中含有测试输入 `.hexex` 文件

进入项目根目录下的 `build/Build/bin/` 目录下，执行：

```
./mc3d_cli --input ../../../tests/resources/fandisk_algohex.hexex --output ./result.hexex
```

成功执行后，会在当前目录下生成 `result.hexex` 结果文件