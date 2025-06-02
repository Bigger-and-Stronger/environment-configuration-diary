# TBB 库配置记录

本文档为配置 TBB 库的记录，[官网安装步骤](https://www.intel.com/content/www/us/en/docs/onetbb/get-started-guide/2021-9/install-onetbb-on-linux-os.html)

---

Canjia Huang <<canjia7@gmail.com>> last update 24/3/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS
- 安装版本：[oneTBB](https://github.com/uxlfoundation/oneTBB)

## 配置步骤

参考 [oneTBB/INSTALL](https://github.com/uxlfoundation/oneTBB/blob/master/INSTALL.md)

1. 将项目下载到本地：

    ```
    git clone https://github.com/oneapi-src/oneTBB.git
    ```

    并进入项目目录：

    ```
    cd oneTBB
    ```

2. 使用 **CMake** 进行配置：

    ```
    mkdir build
    cd build
    ```

    ```
    cmake -DCMAKE_INSTALL_PREFIX=/home/huangcanjia/oneTBB/my_installed_onetbb -DTBB_TEST=OFF ..
    ```

    这里的 `CMAKE_INSTALL_PREFIX` 参数设置了编译后文件生成的位置，可以根据实际情况自定义

3. 编译：

    ```
    cmake --build .
    ```

4. 安装

    ```
    cmake --install .
    ```

5. 安装完毕后在先前指定的 `CMAKE_INSTALL_PREFIX` 路径下会得到所有需要的文件，然后将该目录的下的 “lib” 目录添加到系统变量 `LD_LIBRARY_PATH` 中：

    ```
    vim ~/.bashrc
    ```

    在文件的最后添加（具体路径根据实际情况而定）以新增 `LD_LIBRARY_PATH` 的查找路径：

    ```
    export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:/home/huangcanjia/oneTBB/my_installed_onetbb/lib"
    ```

    保存并退出后，重新加载环境变量：

    ```
    source ~/.bashrc
    ```