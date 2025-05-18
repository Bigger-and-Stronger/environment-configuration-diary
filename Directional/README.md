# Directional 库配置记录

本文档为配置 Directional 库的记录，[[Code]](https://github.com/avaxman/Directional) [[文档]](https://avaxman.github.io/Directional/)

---

Canjia Huang <<canjia7@gmail.com>> last update 15/4/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.5 LTS

## 配置步骤

参考 https://avaxman.github.io/Directional/

1. 将库下载到本地：

    ```
    git clone --recursive https://github.com/avaxman/Directional.git
    ```

    :star: 该库是一个 header-only 的库，不需要额外的配置过程。本文档以下内容为配置附带的 tutorial 代码

2. 进入项目中 tutorial 目录：

    ```
    cd Directional/tutorial
    ```

    新建存放编译文件的目录：

    ```
    mkdir build
    ```

    并进入：

    ```
    cd build
    ```

3. 使用 CMake 进行 configure：

    ```
    cmake -DCMAKE_BUILD_TYPE=Release ..
    ```

    - :warning: 可能出现错误 `Failed to clone repository: 'https://github.com/avaxman/libigl.git'`

        网络原因，多试几次

        出现与 `Fetching Boost` 相关的问题也是相同的处理方式

4. 编译：

    ```
    make -j8
    ```

    - :warning: 可能出现错误 `fatal error: igl/dot_row.h: No such file or directory`

        该文件似乎在最新的 **libigl** 库中被移除，可以在其他仓库中找到 [dot_row.h](https://libigl.github.io/dox/dot__row_8h_source.html), [dot_row.cpp](https://github.com/clo3d/libigl/blob/main/dot_row.cpp)，该文档所在目录也有这两个文件（[dot_row.h](dot_row.h), [dot_row.cpp](dot_row.cpp)）

        将这两个文件复制到 “Directional/tutorial/build/_deps/libigl-src/include/igl/” 目录下
    
    编译完成后会在 “build” 目录下生成各个案例的可执行文件

---

Canjia Huang <<canjia7@gmail.com>> update 25/4/2025

# :apple: macOS

- 操作系统：macOS Sequoia 15.4.1

## 配置步骤

同上

- :warning: 在进行 configure 时可能遇到问题 `Compatibility with CMake < 3.5 has been removed from CMake.`

    可以在 configure 指令中添加选项 `-DCMAKE_POLICY_VERSION_MINIMUM=3.5` 即：

    ```
    cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_POLICY_VERSION_MINIMUM=3.5 ..
    ```

- :warning: 在进行 configure 时 `fetch Boost` 常可能因为网络问题无法成功

    可以对 "Directional/tutorial/build/_deps/boost-cmake-src/CMakeLists.txt" 文件进行修改，具体做法是使用本地安装的 **Boost**，去除 `fetch` 相关指令

    可以使用本文档目录下的 [CMakeLists.txt](CMakeLists.txt) 进行替换
