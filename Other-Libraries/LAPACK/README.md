# lapack, blas, cblas, lapacke 库配置记录

本文档为配置 lapack, blas, cblas, lapacke 库的记录，[[官网]](https://www.netlib.org/lapack/)

---

Canjia Huang <<canjia7@gmail.com>> last update 20/3/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS
- LAPACK 版本：3.12.1

## 配置步骤

参考 [ [1] ]

1. 在 [netlib.org/lapack](https://www.netlib.org/lapack/) 上下载 LAPACK到本地，并解压，会得到 “lapack-3.12.1” 目录（具体目录名称根据实际情况而定），进入该目录：

    ```
    cd lapack-3.12.1/
    ```

2. 因为后续编译时需要该目录下存在 “make.inc” 文件，但该目录下该文件的名称为 “make.inc.example”，所以需要进行复制并改名：

    ```
    cp make.inc.example make.inc
    ```

3. 编译 **blas**：

    ```
    make blaslib
    ```

4. 编译 **cblas**：

    ```
    make cblaslib
    ```

5. 编译 **lapack**：

    ```
    make lapacklib
    ```

6. 编译 **lapacke**：

    ```
    make lapackelib
    ```

[1]: https://zhuanlan.zhihu.com/p/520848641