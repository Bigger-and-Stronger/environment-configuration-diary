# Gmsh 库配置记录

本文档为配置 Gmsh 库的记录，[[官网]](https://gmsh.info)

---

Canjia Huang <<canjia7@gmail.com>> last update 2/4/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤（源码）

1. 下载源码到本地（具体链接根据实际情况而定，可以在 [[官网]](https://gmsh.info) 的 Download the source code 找到）：

    ```
    wget https://gmsh.info/src/gmsh-4.13.1-source.tgz
    ```

    并解压（具体文件名称根据实际情况而定）：

    ```
    tar -xvf gmsh-4.13.1-source.tar
    ```

    进入文件夹：

    ```
    cd gmsh-4.13.1-source
    ```

    该目录下有 “README.txt” 文件，介绍了安装的具体步骤，如下所述

2. 新建存放编译结果的文件夹（如果有 root 权限可以忽略该步骤，直接安装在系统中）：

    ```
    mkdir Gmsh-installed
    ```

3. 创建存放编译文件的目录并进入：

    ```
    mkdir build
    cd build
    ```

4. 使用 CMake 进行 configure：

    - :star: 如果需要在外部调用 Gmsh API 的话，需要添加选项以编译动态链接库：

        ```
        cmake -DENABLE_BUILD_DYNAMIC=1 ..
        ```

    - :star: 如果没有 root 权限，可以设置安装目录为以上新建的 “Gmsh-installed” 目录，并添加选项：

        ```
        cmake -DCMAKE_INSTALL_PREFIX=../Gmsh-installed/ ..
        ```
    
    这里我输入的是：

    ```
    cmake -DENABLE_BUILD_DYNAMIC=1 -DCMAKE_INSTALL_PREFIX=../Gmsh-installed/ ..
    ```

5. 编译：

    ```
    make -j8
    ```

6. 安装：

    ```
    make install
    ```

7. 安装完毕后在先前指定的目录（我这里指定的为 “gmsh-4.13.1-source/Gmsh-installed/”）中会生成可执行文件 “bin/gmsh”，可以进行直接使用

    如果在 C++ 中要使用 **Gmsh** 的话，需要将该目录下的 “include” 目录包含在头文件目录中，并链接 “lib” 目录下的链接库文件 `libgmsh.so`