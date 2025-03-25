# AntTweakBar 库配置记录

本文档为配置 AntTweakBar 库的记录，[[doc]](https://anttweakbar.sourceforge.io/doc/)

---

Canjia Huang <<canjia7@gmail.com>> last update 25/3/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS
- AntTweakBar版本：116

## 配置步骤

参考 [ [1] ]

1. 在 [官网/Download-Install](https://anttweakbar.sourceforge.io/doc/tools_anttweakbar_download.html) 找到最新版本下载链接，并将源码下载到本地（如有更新版本，需要更新以下下载链接）：

    ```
    wget -O AntTweakBar_116.zip https://sourceforge.net/projects/anttweakbar/files/latest/download?source=dlp
    ```

    解压：

    ```
    unzip AntTweakBar_116.zip
    ```

    进入项目目录：

    ```
    cd AntTweakBar/src
    ```

2. 编辑 Makefile 文件：

    ```
    sed -i "s/LINK     	= gcc/LINK     	= g++/" Makefile
    ```

3. 编译：

    ```
    make
    ```

4. 编译完成后，生成的链接库文件存放在 “AntTweakBar/lib/” 目录下，需要将该路径放置在系统变量 `LD_LIBRARY_PATH` 中；项目头文件存放在 “AntTweakBar/include/” 目录下，需要将该路径放置在系统变量 `LIBRARY_PATH` 中

    编辑系统变量：

    ```
    vim ~/.bashrc
    ```

    在文件的最后添加上：

    ```
    export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:/home/huangcanjia/AntTweakBar/lib/"
    export LIBRARY_PATH="${LIBRARY_PATH}:/home/huangcanjia/AntTweakBar/include/"
    ```

    保存并退出后，重新加载环境变量：

    ```
    source ~/.bashrc
    ```

[1]: https://blog.csdn.net/RobinWitch/article/details/127123748