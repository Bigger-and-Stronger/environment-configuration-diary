# CMake 配置记录

本文档为配置 CMake 库的记录

---
Canjia Huang <<canjia7@gmail.com>> last update 27/3/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置记录（无 root）

参考 [ [1] ]

1. 在 [cmake.org](https://cmake.org/download/) 上下载指定版本的 CMake（本文档下载的版本为 3.31.6，具体链接根据实际情况而定）：

    ```
    wget https://github.com/Kitware/CMake/releases/download/v3.31.6/cmake-3.31.6.tar.gz
    ```

2. 解压（具体压缩包名称根据实际情况而定）：

    ```
    tar zxvf cmake-3.31.6.tar.gz
    ```

    并进入目录（具体路径根据实际情况而定）：

    ```
    cd cmake-3.31.6
    ```

3. 配置：

    ```
    ./bootstrap
    ```

    新建安装目录（或者根据实际需要指定安装路径）并进行 configure：

    ```
    mkdir cmake-installed
    ```

    ```
    ./configure --prefix=cmake-installed
    ```

4. 编译安装：

    ```
    make
    make install
    ```

5. 安装完毕后，需要将生成的可执行文件目录 “cmake-3.31.6/cmake-installed/bin”（具体目录根据实际情况而定） 添加到系统变量中：

    ```
    vim ~/.bashrc
    ```

    在文件最后添加：

    ```
    export PATH=/home/huangcanjia/cmake-3.31.6/cmake-installed/bin/:$PATH
    ```

    保存并退出后，重新加载环境变量：

    ```
    source ~/.bashrc
    ```

6. 测试，在终端中查看当前 CMake 版本：

    ```
    cmake --version
    ```

[1]: https://blog.csdn.net/weixin_41317766/article/details/118557246