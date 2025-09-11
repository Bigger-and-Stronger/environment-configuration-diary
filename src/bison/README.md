# bison 配置记录

本文档为配置工具 **bison** 的记录 [[官网]](http://ftp.gnu.org/gnu/bison/)

---

Canjia Huang <<canjia7@gmail.com>> last update 11/9/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤

参考 [1]

1. 下载安装包：

    ```
    wget http://ftp.gnu.org/gnu/bison/bison-3.2.1.tar.gz
    ```

    并解压缩：

    ```
    tar -zxvf bison-3.2.1.tar.gz
    ```

    进入目录：

    ```
    cd bison-3.2.1
    ```

2. 新建用于存放安装结果的目录：

    ```
    mkdir bison-installed
    ```

3. 进行 configure（指定安装目录，为先前新建的目录的绝对路径，具体根据实际情况而定）：

    ```
    ./configure --prefix=/home/huangcanjia/bison-3.2.1/bison-installed
    ```

4. 编译：

    ```
    make
    ```

5. 安装：

    ```
    make install
    ```

6. 安装完毕后在 `bison-3.2.1/bison-installed/bin` 目录下会有可执行文件 **bison**，可以将该路径添加到系统环境变量中方便使用：

    ```
    vim ~/.bashrc
    ```

    在文件最后添加（具体路径根据实际情况而定）：

    ```
    export LD_LIBRARY_PATH=/home/huangcanjia/petsc/arch-linux-c-debug/lib/:$LD_LIBRARY_PATH
    ```

    保存并退出，然后重新加载环境变量：

    ```
    source ~/.bashrc
    ```

    此时在任意目录下，可使用 `bison` 指令
    

[1]: https://blog.csdn.net/Mculover666/article/details/118934814