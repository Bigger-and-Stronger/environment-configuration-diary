# OpenMPI 库配置记录

本文档为配置 OpenMPI 库的记录，[[官网]](https://www.open-mpi.org/)

---

Canjia Huang <<canjia7@gmail.com>> last update 28/3/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.5 LTS

## 配置步骤（无 root）

参考 [ [1] ]

1. 在 [官网/Download](https://www.open-mpi.org/software/ompi/v5.0/) 下载合适的版本，如我这里下载（具体链接根据实际情况而定）：

    ```
    wget https://download.open-mpi.org/release/open-mpi/v5.0/openmpi-5.0.7.tar.gz
    ```

    下载完毕后进行解压（具体安装包名称根据实际情况而定）：

    ```
    tar -xzvf openmpi-5.0.7.tar.gz
    ```

    进入项目目录（具体目录名称根据实际情况而定）：

    ```
    cd openmpi-5.0.7
    ```

2. 新建用于存放编译结果的文件夹：

    ```
    mkdir openmpi-installed
    ```

   进行 configure（选项 `prefix` 的具体路径设定为上面:point_up_2:新建的目录 "openmpi-installed" 或其他目录，需要根据实际情况而定，并且设定为绝对路径）：

    ```
    ./configure --prefix=/home/huangcanjia/openmpi-5.0.7/openmpi-installed/
    ```

3. 编译：

    ```
    make all
    ```

4. 安装：

    ```
    make install
    ```

5. 安装结果会出现在上述指定的 `prefix` 路径下

    最后需要将编译结果的 “bin” 目录添加到系统环境变量 `PATH` 中，将 “lib” 目录添加到系统环境变量 `LD_LIBRARY_PATH` 中： 

    ```
    vim ~/.bashrc
    ```

    在文件的最后添加（具体路径需要根据实际情况进行调整）：

    ```
    export PATH=/home/huangcanjia/openmpi-5.0.7/openmpi-installed/bin:$PATH
    export LD_LIBRARY_PATH=/home/huangcanjia/openmpi-5.0.7/openmpi-installed/lib:$LD_LIBRARY_PATH
    ```

    - :bangbang: 如果系统中已经有安装其他版本的 **OpenMPI**，设置系统变量目录时要将自己安装的目录放在原先系统变量的前面，即应按上面给出的示例进行设置，而不能设置为：

        ```
        export PATH="$PATH:/home/huangcanjia/openmpi-5.0.7/openmpi-installed/bin"
        export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/home/huangcanjia/openmpi-5.0.7/openmpi-installed/lib"
        ```

    保存并退出后，重新加载环境变量：

    ```
    source ~/.bashrc
    ```

## 测试

1. 在终端中输入：

    ```
    which mpirun
    ```
    ```
    mpirun
    ```

[1]: https://blog.csdn.net/zyh19980527/article/details/107790695