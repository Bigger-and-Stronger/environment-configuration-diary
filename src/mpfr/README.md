# mpfr 库配置记录

本文档为配置 mpfr 库的记录，[[官网]](https://www.mpfr.org)

---

Canjia Huang <<canjia7@gmail.com>> last update 15/4/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.5 LTS

## 预备步骤

需要安装 **gmp** 库，具体可以参考 [gmp 库配置记录](../gmp/)

## 配置步骤（无 root，源码编译）

参考 [ [1] ]

1. 从 https://www.mpfr.org/mpfr-current/#download 上下载源码（具体链接根据实际情况而定）：

    ```
    wget https://www.mpfr.org/mpfr-current/mpfr-4.2.2.tar.xz
    ```

    并解压（具体文件名称根据实际情况而定）：

    ```
    tar -xvf mpfr-4.2.2.tar.xz
    ```

    进入项目目录（具体目录名称根据实际情况而定）：

    ```
    cd mpfr-4.2.2
    ```

2. 新建存放编译结果的目录：

    ```
    mkdir mpfr-installed
    ```

    进行 configure（这里的 `prefix` 选项设置为刚才新建的目录的绝对路径，`with-gmp` 选项设置为 **gmp** 库的安装目录）：

    ```
    ./configure --prefix=/home/huangcanjia/mpfr-4.2.2/mpfr-installed/ --with-gmp=/home/huangcanjia/gmp-6.3.0/
    ```

3. 编译：

    ```
    make
    ```

4. 安装：

    ```
    make install
    ```

[1]: https://www.oryoy.com/news/ubuntu-qing-song-an-zhuang-mpfr-kai-qi-gao-xiao-shu-xue-ji-suan-de-kuai-jie-zhi-lu.html