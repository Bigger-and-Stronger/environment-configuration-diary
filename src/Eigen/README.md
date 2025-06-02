# Eigen 库配置记录

本文档为配置 Eigen 库的记录，[[官网]](https://www.graphics.rwth-aachen.de/software/openmesh/)

---

Canjia Huang <<canjia7@gmail.com>> last update 18/3/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS
- Eigen 版本：3.4.90，其他不同版本可在 [gitlab/libeigen](https://gitlab.com/libeigen/eigen/-/releases/?before=eyJyZWxlYXNlZF9hdCI6IjIwMTYtMTItMDYgMTE6NDM6MDAuMDAwMDAwMDAwICswMDAwIiwiaWQiOiIxMTE0MzE2In0) 找到

## 配置步骤（无 root）

该配置步骤为无 root 权限下的配置方案，参考 [ [1] ]

1. 将最新的 **Eigen** 库下载到本地：

    ```
    git clone https://gitlab.com/libeigen/eigen.git
    ```

    进入库目录：

    ```
    cd eigen
    ```

2. 新建编译临时目录 “build” 以及存放编译结果的目录 “eigen-installed”（具体名称可以自由选择，此处以此为例）：

    ```
    mkdir build
    mkdir eigen-installed
    ```

    并进入目录：

    ```
    cd build
    ```

3. 使用 CMake 进行 configure，并设置安装目录为上面新建的目录（具体根据实际情况调整）：

    ```
    cmake .. -DCMAKE_INSTALL_PREFIX=../eigen-installed
    ```

4. 编译安装：

    ```
    make install
    ```

5. 安装完毕后可以在 “eigen/eigen-installed” 目录中找到相关文件

    <!-- 需要将相关目录设置到系统环境变量中：

    ```
    vim ~/.bashrc
    ```

    在文件的最后添加 “eigen/eigen-installed/include/eigen3” 目录（具体以实际情况为准）：

    ```
    export CPATH=${CPATH}:/home/huangcanjia/eigen/eigen-installed/include/eigen3
    ```

    保存并退出后，重新加载环境变量：

    ```
    source ~/.bashrc
    ``` -->

[1]: https://blog.csdn.net/weixin_40966959/article/details/132275847