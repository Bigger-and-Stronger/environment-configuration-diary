# binutils 配置记录

本文档为配置 binutils 的过程记录文档

---

Canjia Huang <<canjia7@gmail.com>> update 20/6/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤

参考 [ [1] ]

1. 在网页 http://ftp.gnu.org/gnu/binutils/ 上下载对应版本的 binutils（我这里选择的版本是 2.35），即输入：
    ```
    https://ftp.gnu.org/gnu/binutils/binutils-2.35.tar.xz
    ```

    下载完毕后解压缩：
    ```
    tar -xvf binutils-2.35.tar.xz
    ```

    并进入该目录：
    ```
    cd binutils-2.35/
    ```

2. 新建存放安装结果的目录：
    ```
    mkdir mkdir binutils-installed
    ```

3. 进行 configure，需指定选项 `prefix` 为前面存放安装结果的目录的绝对路径（具体路径根据实际情况而定）：
    ```
    ./configure --prefix=/home/huangcanjia/binutils-2.35/binutils-installed/
    ```

4. 编译：
    ```
    make -j
    ```

   - :warning: 可能出现问题：`error: ‘DEFAULT_GENERATE_ELF_STT_COMMON’ undeclared here (not in a function)`

       参考 [ [2] ]，在终端中输入：

       ```
       unset C_INCLUDE_PATH
       ```

       再重新进行编译即可

5. 安装：
    ```
    make install
    ```

6. 将安装结果目录中的 “bin” 目录添加到系统 `PATH` 变量中，即：
    ```
    vim ~/.bashrc
    ```

    在最后添加（具体路径根据实际情况而定）：
    ```
    export PATH=/home/huangcanjia/binutils-2.35/binutils-installed/bin/:$PATH
    ```

    保存并退出后，重新载入环境变量：
    ```
    source ~/.bashrc
    ```

7. 在终端中输入：

    ```
    ld --version | head -n1
    ```

    如果输出的 binutils 的版本正确的话，则安装成功

[1]: https://blog.csdn.net/u010835747/article/details/109612586
[2]: https://blog.csdn.net/goodnameused/article/details/138216579