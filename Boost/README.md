# Boost 库配置记录

本文档为配置 Boost 库的记录，[[官网]](https://www.boost.org)

---

Canjia Huang <<canjia7@gmail.com>> last update 15/4/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.5 LTS

## 配置步骤（无 root）

参考 [ [1] ]

1. 从 https://www.boost.org/users/download/ 上下载需要的 **Boost** 版本，如（具体链接根据实际情况而定）：

    ```
    wget https://archives.boost.io/release/1.88.0/source/boost_1_88_0.tar.gz
    ```

2. 解压（具体文件名称根据实际情况而定）：

    ```
    tar -xvf boost_1_88_0.tar
    ```

    并进入库目录：

    ```
    cd boost_1_88_0
    ```

3. configure：

    ```
    ./bootstrap.sh --with-libraries=all
    ```

4. 安装：

    ```
    ./b2 install --prefix=.
    ```

5. 添加相应的环境变量：

    ```
    vim ~/.bashrc
    ```

    在文件的最后添加（具体路径根据实际情况而定）：

    ```
    export BOOST_ROOT=/home/huangcanjia/boost_1_88_0/
    export BOOST_INCLUDEDIR=$BOOST_ROOT/boost
    export BOOTS_LIBRARYDIR=$BOOST_ROOT/lib
    export LIBRARY_PATH=$BOOST_ROOT:$LIBRARY_PATH
    export LD_LIBRARY_PATH=$BOOST_ROOT:$LD_LIBRARY_PATH
    ```

    保存并退出，然后重新加载环境变量：

    ```
    source ~/.bashrc
    ```

[1]: https://blog.csdn.net/qq_51777284/article/details/134747055