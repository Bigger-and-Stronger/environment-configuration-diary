# fpm 配置记录

本文档为配置 fpm (Fortran Package Manager) 的记录，[[官网]](https://fpm.fortran-lang.org/index.html)

---

Canjia Huang <<canjia7@gmail.com>> last update 8/4/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS
- gcc version：10.5.0

## 配置步骤（直接下载可执行文件）

参考 [fortan-lang.org/install](https://fpm.fortran-lang.org/install/index.html)

1. 新建存放该可执行文件的目录：

    ```
    mkdir fpm
    ```

    并进入：

    ```
    cd fpm
    ```

2. 在 [fpm/releases](https://github.com/fortran-lang/fpm/releases) 上下载适合的版本，我这里下载的是 `linux-x86_64-gcc-12` 的版本（具体版本及下载链接根据实际情况而定）：

    ```
    wget https://github.com/fortran-lang/fpm/releases/download/v0.11.0/fpm-0.11.0-linux-x86_64-gcc-12
    ```

    为了方便使用，将该可执行文件改名为 “fpm”（具体原始可执行文件名称根据实际情况而定）：

    ```
    mv fpm-0.11.0-linux-x86_64-gcc-12 fpm
    ```

3. 更改该可执行文件权限：

    ```
    chmod +x fpm
    ```

    此时该可执行文件就可以执行了：

    ```
    ./fpm
    ```

4. 为了方便全局调用，可以将存放该可执行文件的目录添加到系统环境变量中：

    ```
    vim ~/.bashrc
    ```

    在文件的最后添加（具体路径根据实际情况而定，就是上面新建的存放可执行文件的目录）：

    ```
     export PATH=/home/huangcanjia/fpm/:$PATH
    ```

    保存并退出后，重新加载环境变量：

    ```
    source ~/.bashrc
    ```

    此时应该可以在任意位置使用指令 `fpm` 来调用该可执行文件