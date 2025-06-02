# p7zip 配置记录

本文档为配置 7z 压缩包解压工具 **p7zip** 的安装配置记录，[[Github]](https://github.com/p7zip-project/p7zip)

---
Canjia Huang <<canjia7@gmail.com>> last update 28/3/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置记录

参考 [p7zip/README](https://github.com/p7zip-project/p7zip/blob/master/README.md)，[ [1] ]

1. 下载源码：

    ```
    git clone https://github.com/p7zip-project/p7zip.git
    ```

    并进入目录：

    ```
    cd p7zip
    ```

2. 编译 **7zz**（功能较多，如果只需要解压 “.7z” 文件，也可以安装 **7za** 或 **7zr**）：

    ```
    cd CPP/7zip/Bundles/Alone2/
    make -f makefile.gcc
    ```

3. 安装：

   - 如果有 root 权限的话，可以安装：

        ```
        sudo make -f makefile.gcc install
        ```

   -  如果没有 root 权限的话

        编译完成的可执行文件 **7zz** 存放在 “p7zip/CPP/7zip/Bundles/Alone2/_o/bin/” 目录下（具体路径依据实际情况为准），需要将该路径添加到系统变量 `PATH` 中：

        ```
        vim ~/.bashrc
        ```

        在文件的最后添加：

        ```
        export PATH=/home/huangcanjia/p7zip/CPP/7zip/Bundles/Alone2/_o/bin/:$PATH
        ```

        并重新加载环境变量：

        ```
        source ~/.bashrc
        ```

4. 测试，在任意目录下，在终端中输入：

    ```
    7zz
    ```

[1]: https://blog.csdn.net/weixin_42863990/article/details/125263585