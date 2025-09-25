# ALGLIB 库配置记录

本文档为配置 ALGLIB 库的记录，[[官网]](https://www.alglib.net)

---

Canjia Huang <<canjia7@gmail.com>> last update 8/4/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS
- ALGLIB version：4.04.0 for C++（Free Edition）

## 配置步骤（root）

如果有 root 权限的话，可能可以直接执行安装指令：

```
sudo apt install libalglib-dev
```

## 配置步骤（源码编译）

1. 下载源码（具体链接参考 https://www.alglib.net/download.php 中给出）：

    ```
    wget https://www.alglib.net/translator/re/alglib-4.04.0.cpp.gpl.tgz
    ```

    并解压（具体文件名称根据实际情况而定）：

    ```
    tar zxvf  alglib-4.04.0.cpp.gpl.tgz
    ```

    进入目录：

    ```
    cd alglib-cpp
    ```

:star: 如果只是希望在自己的项目中使用，将 “alglib-cpp/src” 中的文件添加到项目中即可

## 配置步骤（链接库）

如果希望得到编译的动态链接库来使用，可以使用基于 deb 的安装方法

1. 下载 deb 安装包（此处版本下载的 alglib 版本为 3.14）

    ```
    apt download libalglib3.14
    ```

2. 新建目录，并解压：

    ```
    mkdir alglib-3.14-deb
    dpkg -x libalglib3.14_3.16.0-1build1_amd64.deb alglib-3.14-deb/
    ```

3. 完成后，动态链接库位于目录 "/home/huangcanjia/alglib-3.14-deb/usr/lib/x86_64-linux-gnu" 下（具体路径根据实际情况而定），可以将其添加至系统环境变量 `LD_LIBRARY_PATH` 中

<!-- > [!CAUTION]
> 以下方法可能有误，可能会导致生成的链接库中没有所需的符号！！！

:star: 如果需要编译生成链接库来使用，则继续进行以下配置步骤

1. 新建存放编译文件和动态库的目录：

    ```
    mkdir obj
    mkdir lib
    ```

2. 编译所有文件，在终端中输入：

    ```
    for cpp_file in src/*.cpp; do
        g++ -c -fPIC -I./src "$cpp_file" -o "obj/$(basename "$cpp_file" .cpp).o"
    done
    ```

3. 打包生成动态链接库文件：

    ```
    g++ -shared -o lib/libalglib.so obj/*.o
    ```

    此时在 “alglib-cpp/lib” 目录下会生成动态链接库文件 `libalglib.so`

4. 将动态链接库文件所在目录添加到系统环境变量中：
    ```
    vim ~/.bashrc
    ```

    在文件的最后添加（具体路径根据实际情况而定，即上面生成的链接库所在目录）：

    ```
    export LD_LIBRARY_PATH=/home/huangcanjia/alglib-cpp/lib/:$LD_LIBRARY_PATH
    ```

    保存并退出，重新加载系统环境变量：

    ```
    source ~/.bashrc
    ``` -->