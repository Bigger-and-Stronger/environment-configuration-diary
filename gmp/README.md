# gmp 库配置记录

本文档为配置 gmp 库的记录，[[官网]](https://gmplib.org)

---

Canjia Huang <<canjia7@gmail.com>> last update 14/4/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.5 LTS

## 配置步骤

参考 [ [1] ]

1. 从 [[官网]](https://gmplib.org) 上下载（具体下载链接根据实际情况而定）：

    ```
    wget https://gmplib.org/download/gmp/gmp-6.3.0.tar.xz
    ```

2. 解压（具体文件名称根据实际情况而定）：

    ```
    tar -xvf gmp-6.3.0.tar.xz
    ```

    并进入项目目录：

    ```
    cd gmp-6.3.0
    ```

3. 新建存放编译结果的目录：

    ```
    mkdir gmp-installed
    ```

    进行 configure（`--prefix` 设置为刚新建的目录的绝对路径）：

    ```
    ./configure --prefix=/home/huangcanjia/gmp-6.3.0/gmp-installed/  --enable-cxx
    ```

4. 编译：

    ```
    make
    ```

    编译完成后，检查编译：

    ```
    make check
    ```

5. 安装：

    ```
    make install
    ```

[1]: https://blog.csdn.net/qq_41956187/article/details/129170869