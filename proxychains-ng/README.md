# proxychains-ng 配置记录

本文档为配置 Linux 命令行代理 proxychain-ng 的记录 [ [github] ](https://github.com/rofl0r/proxychains-ng)

---
Canjia Huang <<canjia7@gmail.com>> update 18/5/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤

参考 [ [1] ]

1. 将 [github/proxychains-ng](https://github.com/rofl0r/proxychains-ng) 下载到本地：

    ```
    git clone https://github.com/rofl0r/proxychains-ng.git
    ```

    并进入项目目录：

    ```
    cd proxychains-ng
    ```

2. 进行 configure：

    ```
    ./configure
    ```

    - :warning: 如果没有 root 权限，为了后续方便，可以指定系统 configure 文件目录为该目录，即改为执行（具体目录设置为项目的绝对目录）：

        ```
        ./configure --sysconfdir=/home/huangcanjia/proxychains-ng/
        ```

3. 编译：

    ```
    make -j
    ```

    编译完成后会在该目录下生成 `proxychains4` 的可执行文件

4. 安装：

    ```
    sudo make install
    ```

    - :warning: 如果没有 root 权限，会导致后续安装失败，但关系不大，仍然可以通过手动进入该目录来调用可执行文件 `./proxychains4`

<!-- 
或者将该目录添加到系统 Path 变量中：

```
vim ~/.bashrc
```

在文件的最后添加（其中的路径设置为 proxychains-ng 项目的路径）：
```
export PATH=/home/huangcanjia/proxychains-ng/:$PATH
export LD_LIBRARY_PATH=/home/huangcanjia/proxychains-ng/:$LD_LIBRARY_PATH
```

保存并退出后，重新载入环境变量：

```
source ~/.bashrc
```

设置完成后，可以直接使用 `proxychains4` 来启动该可执行文件 
-->

5. 创建代理配置文件，如果在 configure 过程中设置了 `sysconfdir` 选项，则在设置的目录下创建文件：

    ```
    vim proxychains.conf
    ```

    如果有 root 权限并进行了安装，则配置文件已在 "etc/proxychains.conf" 处

    在该文件中输入（具体情况根据实际代理而定）：

    ```
    [ProxyList]
    socks5 127.0.0.1 7890
    http   127.0.0.1 7890
    ```

    保存并退出

## 测试

参考 [ [2] ]

1. 在不使用代理的情况下，即输入：

    ```
    curl www.httpbin.org/ip
    ```

2. 以及使用代理的情况下，即输入：

    ```
    ./proxychains4 curl www.httpbin.org/ip
    ```

应该会出现不一样的 IP


[1]: https://zhuanlan.zhihu.com/p/166375631
[2]: https://www.cnblogs.com/mwq1024/p/11582003.html