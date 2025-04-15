# gmp 库配置记录

本文档为配置 gmp 库的记录，[[官网]](https://gmplib.org)

---

Canjia Huang <<canjia7@gmail.com>> last update 14/4/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.5 LTS

## 配置步骤（无 root）

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
    ./configure --prefix=/home/huangcanjia/gmp-6.3.0/gmp-installed/ --enable-cxx
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

## 常见错误

- :warning: 如果在项目中使用时，在编译过程中出现错误 `/usr/bin/ld: /home/huangcanjia/gmp-6.3.0/gmp-installed/lib/libgmp.a(mul_fft.o): relocation R_X86_64_32 against .rodata.str1.1 can not be used when making a PIE object; recompile with -fPIE`

    首先进入 **gmp** 项目的目录，然后清理先前的 **gmp** 库的安装：
    
    ```
    make distclean || ./configure --clean
    ```

    并把编译完成的目录 “gmp-installed” 删掉并重新新建目录（重要 :bangbang:）

    进行 configure 时启用位置无关代码，即需要添加选项 `CFLAGS="-fPIC -O2"`，即：

    ```
    ./configure CFLAGS="-fPIC -O2" --prefix=/home/huangcanjia/gmp-6.3.0/gmp-installed/ --enable-cxx
    ```

    然后继续后续的步骤，重新编译并安装

[1]: https://blog.csdn.net/qq_41956187/article/details/129170869