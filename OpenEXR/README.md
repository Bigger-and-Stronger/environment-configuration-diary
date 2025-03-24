# OpenEXR 库配置记录

本文档为配置 OpenEXR 库的记录，[官网](https://openexr.com/en/latest/)

---

Canjia Huang <<canjia7@gmail.com>> last update 24/3/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS
- 安装版本：

## 配置步骤（源码编译）

参考 [官网配置步骤](https://openexr.com/en/latest/install.html) 此处使用 [源码编译步骤](https://openexr.com/en/latest/install.html#build-from-source)，以便在无 root 环境下进行配置

1. 将项目 [openexr](https://github.com/AcademySoftwareFoundation/openexr) 下载到本地：

    ```
    git clone https://github.com/AcademySoftwareFoundation/openexr.git
    ```

    并进入项目目录：

    ```
    cd openexr
    ```

2. 新建安装库和头文件的目标目录（该目录名称可以自定义，但后续使用到该目录时需要自行替换）：

    ```
    mkdir installed-openexr
    ```

3. 新建临时存储文件夹并进入：

    ```
    mkdir build
    cd build
    ```

4. 使用 **CMake** 进行 configure（此处的 `install-prefix` 设置路径需与前面的相同）：

    ```
    cmake -DCMAKE_INSTALL_PREFIX=../installed-openexr/  ..
    ```

5. 编译：

    ```
    cmake --build . --target install --config Release
    ```

6. 安装完毕后在先前指定的 `CMAKE_INSTALL_PREFIX` 路径下会得到所有需要的文件，然后将该目录的下的 “lib” 目录添加到系统变量 `LD_LIBRARY_PATH` 中：

    ```
    vim ~/.bashrc
    ```

    在文件的最后添加（具体路径根据实际情况而定）以新增 `LD_LIBRARY_PATH` 的查找路径：

    ```
    export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:/home/huangcanjia/openexr/installed-openexr/lib"
    ```

    保存并退出后，重新加载环境变量：

    ```
    source ~/.bashrc
    ```
