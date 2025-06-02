# Minpack 库配置记录

本文档为配置 Minpack 库的记录，[[Github]](https://github.com/fortran-lang/minpack)

---

Canjia Huang <<canjia7@gmail.com>> last update 8/4/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤（root）

如果有 root 权限的话，可能可以直接执行安装指令：

```
sudo apt install minpack-dev
```

## 配置步骤（fpm）

参考 [minpack/README-build-with-fpm](https://github.com/fortran-lang/minpack?tab=readme-ov-file#building-with-fpm)

该库使用 Fortran 语言编写，所以需要安装该语言的编译管理器，如 **fpm**，安装配置过程参考 [fpm 配置记录](../fpm/)

1. 将库项目下载到本地：

    ```
    git clone https://github.com/fortran-lang/minpack
    ```

    并进入项目目录：

    ```
    cd minpack
    ```

2. 使用 **fpm** 进行构建：

    ```
    fpm build
    ```

    构建完成后可以使用 **fpm** 进行测试：

    ```
    fpm test
    ```

## 编译链接库

如果有的项目需要使用 **minpack** 的链接库 `libminpack`，需要进行编译生成

1. 在该库项目目录下新建 Makefile 文件：

    ```
    vim Makefile
    ```

    在文件中输入：

    ```
    FC = gfortran
    FFLAGS = -O2 -fPIC

    SRCS = $(wildcard *.f)
    OBJS = $(SRCS:.f=.o)

    libminpack.so: $(OBJS)
            $(FC) -shared -Wl,-soname,libminpack -o $@ $^ -lblas -llapack

    clean:
            rm -f *.o *.so*
    ```

    保存并退出

2. 进行编译：

    ```
    make
    ```

    编译完成后会在目录下生成 `libminpack.so` 文件

3. 将链接库所在目录添加到系统环境变量中：

    ```
    vim ~/.bashrc
    ```

    在文件的最后添加（具体路径根据实际情况而定，即上面生成的链接库所在目录）：

    ```
    export LD_LIBRARY_PATH=/home/huangcanjia/minpack/:$LD_LIBRARY_PATH
    ```

    保存并退出，重新加载系统环境变量：

    ```
    source ~/.bashrc
    ```