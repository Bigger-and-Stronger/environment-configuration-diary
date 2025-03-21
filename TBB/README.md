# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤

参考 [ [1] ]

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
    cmake ..
    ```

3. 编译：

    ```
    make -j8
    ```

4. 安装

    - 如果有 root 权限的话，执行：

        ```
        sudo make install
        ```

    - 如果没有 root 权限，需要在环境变量中链接相应的目录，参考 [ [2] ]

        编辑环境变量：

        ```
        vim ~/.bashrc
        ```

        编译结束后的许多生成文件在 “xxx/oneTBB/build/gnu_10.5_cxx11_64_relwithdebinfo/” 目录下（具体路径根据实际情况而定），将该路径添加到 “~/.bashrc” 文件最后（具体路径根据实际情况而定）：

        ```
        export LD_LIBRARY_PATH=/home/huangcanjia/oneTBB/build/gnu_10.5_cxx11_64_relwithdebinfo:$LD_LIBRARY_PATH
        ```

[1]: https://blog.csdn.net/weixin_42973508/article/details/111681426
[2]: https://blog.csdn.net/qq_39779233/article/details/126284595