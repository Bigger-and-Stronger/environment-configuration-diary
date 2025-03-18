# OpenMesh 库配置记录

本文档为配置 OpenMesh 库的记录，[[官网]](https://www.graphics.rwth-aachen.de/software/openmesh/)

---

Canjia Huang <<canjia7@gmail.com>> last update 18/3/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6

## 配置步骤

参考 [[官网/Download]](https://www.graphics.rwth-aachen.de/software/openmesh/download/) [[1]](https://www.oryoy.com/news/ubuntu-xi-tong-qing-song-shang-shou-pei-zhi-openmesh-yi-bu-dao-wei-zhi-nan.html)

1. 将 OpenMesh 源码下载到本地，可以使用 `git clone`：

    ```
    git clone --recursive https://gitlab.vci.rwth-aachen.de:9000/OpenMesh/OpenMesh.git
    ```

    并进入该文件夹：

    ```
    cd OpenMesh
    ```

2. 在项目根目录新建 “build” 文件夹，并进入，使用 CMake 进行生成：

    ```
    cd build
    cmake ..
    ```

    过程中可能需要安装一些常用的依赖库

3. 生成完毕后，进行编译：

    ```
    make
    ```

4. 编译完成后，进行安装（需要 root 权限）：

    ```
    sudo make install
    ```