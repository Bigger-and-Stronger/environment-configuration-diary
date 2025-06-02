# PETSc 库配置记录

本文档为配置 PETSc 库的记录，[[官网]](https://petsc.org/release/)

---

Canjia Huang <<canjia7@gmail.com>> last update 9/4/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤（root）

如果有 root 权限的话，可能可以直接执行安装指令：

```
sudo apt install petsc-dev
```

## 配置步骤（源码编译）

参考 [petsc.org/install-tutorial](https://petsc.org/release/install/install_tutorial/#downloading-source)

1. 将库项目下载到本地：

    ```
    git clone -b release https://gitlab.com/petsc/petsc
    ```

    并进入目录：

    ```
    cd petsc
    ```

2. 新建存放编译文件的目录：

    ```
    mkdir petsc-installed
    ```

    并进行 configure

    ```
    ./configure --prefix=petsc-installed --download-mpich --download-fblaslapack
    ```

3. 编译：

    ```
    make all check
    ```

    export LD_LIBRARY_PATH=/home/huangcanjia/petsc/arch-linux-c-debug/lib/:$LD_LIBRARY_PATH