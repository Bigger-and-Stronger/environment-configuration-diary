# gsl 库配置记录

[[官网]](https://www.gnu.org/software/gsl/) [[github]](https://github.com/ampl/gsl)

---

Canjia Huang <<canjia7@gmail.com>> last update 13/9/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤

参考 [README](https://github.com/ampl/gsl/blob/master/README.md)

1. 从 github 上下载：

    ```
    git clone https://github.com/ampl/gsl.git
    ```

    并进入目录：

    ```
    cd gsl
    ```

2. 新建存放安装结果的目录：

    ```
    mkdir gsl-installed
    ```

3. 进行 configure，并指定安装目录为先前创建的目录（具体路径根据实际情况而定）：

    ```
    ./configure --prefix=/home/huangcanjia/gsl/gsl-installed
    ```

4. 编译：

    ```
    make
    ```

5. 安装：

    ```
    make install
    ```

6. 为方便后续使用，可以将 `gsl-installed` 目录添加到系统环境变量 `GSL_ROOT_DIR` 中，即：

    `vim ~/.bashrc`

    在文件的最后输入：

    `export GSL_ROOT_DIR=/home/huangcanjia/gsl/gsl-installed`

    保存并退出后，重新载入系统环境变量：

    `source ~/.bashrc`

在 CMake 中使用可以使用文件 [FindGSL.cmake](https://github.com/nest/nest-simulator/blob/4dcf79c78dd56e70758c2ad5f4de9cb6108bbff0/cmake/FindGSL.cmake#L4)