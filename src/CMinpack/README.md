# CMinpack 库配置记录

本文档为配置 CMinpack 库的记录，[[官网]](https://devernay.github.io/cminpack/)

基于 Fortran 的版本 **Minpack** 的配置可以参考 [Minpack 库配置记录](../Minpack/)

---

Canjia Huang <<canjia7@gmail.com>> last update 25/9/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤

1. 在官网上下载源码（此处下载的版本为 1.3.11）：

    ```
    wget https://github.com/devernay/cminpack/archive/v1.3.11.tar.gz
    ```

    并解压：

    ```
    tar -zxvf v1.3.11.tar.gz
    ```

    并进入目录：

    ```
    cd cminpack-1.3.11
    ```

2. 新建存放编译结果的目录并进入：

    ```
    mkdir build && cd build
    ```

3. 使用 CMake 进行 configure：

    ```
    cmake ..
    ```

    - :star: 如果希望编译出动态链接库，可以添加 CMake 选择 `-DBUILD_SHARED_LIBS=ON`

4. 编译：

    ```
    make -j
    ```

    编译完成后会在 “build” 目录下生成 “.a” 链接库文件