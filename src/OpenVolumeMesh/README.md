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

    - 默认生成的是静态链接库（\*.a, \*.lib），如果希望生成动态链接库（\*.dll, \*.so, \*.dylib），需要设置 CMake 选项 `BUILD_SHARED_LIBS` 为 true，即：

        ```
        cmake -DBUILD_SHARED_LIBS=true .
        ```

        编译的链接库在该目录下的 “Build/lib” 目录下

3. 编译：
    ```
    make -j
    ```