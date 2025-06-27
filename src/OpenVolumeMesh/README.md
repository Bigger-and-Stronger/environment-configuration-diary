# OpenVolumeMesh 配置记录

本文档为配置 OpenVolumeMesh 的记录 [[overview]](https://www.graphics.rwth-aachen.de/software/openvolumemesh/) [[download]](https://www.graphics.rwth-aachen.de/software/openvolumemesh/download/)

---

Canjia Huang <<canjia7@gmail.com>> update 27/6/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤

1. 将项目下载到本地：
    ```
    git clone --recursive https://www.graphics.rwth-aachen.de:9000/OpenVolumeMesh/OpenVolumeMesh.git
    ```

    并进入项目目录：
    ```
    cd OpenVolumeMesh
    ```

2. 使用 CMake 进行 configure：
    ```
    cmake .
    ```

3. 编译：
    ```
    make -j
    ```