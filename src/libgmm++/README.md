# libgmm++ 库配置记录

[官网](http://getfem.org/gmm.html)

---

Canjia Huang <<canjia7@gmail.com>> last update 1/10/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤 (deb)

该库是一个仅头文件的库，可以通过以下方式直接下载

1. 下载 dev 安装包：

    ```
    apt download libgmm++-dev
    ```

2. 新建存放安装内容的目录：

    ```
    mkdir libgmm++
    ```

3. 解压到该目录（具体文件名称和路径根据实际情况而定）：

    ```
    dpkg -x libgmm++-dev_5.3+dfsg1-3build2_amd64.deb libgmm++
    ```

4. 解压完成后，在目录 “libgmm++-deb/usr/include” 下就有相关的头文件