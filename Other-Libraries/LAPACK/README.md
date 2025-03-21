# lapack, blas, cblas, lapacke 库配置记录

本文档为配置 lapack, blas, cblas, lapacke 库的记录，[[官网]](https://www.netlib.org/lapack/)

---

Canjia Huang <<canjia7@gmail.com>> last update 20/3/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS
- LAPACK 版本：3.12.1

## 配置步骤

参考 [ [1] ]

1. 在 [netlib.org/lapack](https://www.netlib.org/lapack/) 上下载 LAPACK （已经包含着 blas、cblas、lapacke）到本地，并解压，会得到 “lapack-3.12.1” 目录（具体目录名称根据实际情况而定），进入该目录：

    ```
    cd lapack-3.12.1/
    ```

2. 因为后续编译时需要该目录下存在 “make.inc” 文件，但该目录下该文件的名称为 “make.inc.example”，所以需要复制该文件并改名：

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

7. 编译完成后的静态库目录为项目根目录 “xxx/lapack-3.12.1/”（具体路径根据实际情况而定），该目录下应该有以下静态库文件：

    ```
    libcblas.a
    liblapack.a
    liblapacke.a
    librefblas.a
    ```

    cblas 库的头文件所在目录为 “xxx/lapack-3.12.1/CBLAS/include”（具体路径根据实际情况而定）
    lapacke 库的头文件所在目录为 “xxx/lapack-3.12.1/LAPACKE/include”（具体路径根据实际情况而定）

8. 将静态库和头文件目录存放在系统变量中，编辑 “～/.bashrc” 文件：

    ```
    vim ~/.bashrc
    ```

    在文件的最后添加上（具体路径根据上一步骤以及实际情况而定）：

    ```
    export LIBRARY_PATH=$LIBRARY_PATH:/home/huangcanjia/lapack-3.12.1
    export C_INCLUDE_PATH=$C_INCLUDE_PATH:/home/huangcanjia/lapack-3.12.1/CBLAS/include:/home/huangcanjia/lapack-3.12.1/CBLAS/include
    ```

    保存并退出后，执行：

    ```
    source ~/.bashrc
    ```

[1]: https://zhuanlan.zhihu.com/p/520848641