# TCL, TK 解释器配置记录

本文档为配置 TCL, TK 解释器的记录，[[官网]](https://www.tcl-lang.org)

---

Canjia Huang <<canjia7@gmail.com>> last update 18/4/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.5 LTS

## 配置步骤（root）

如果有 root 权限的话，可能可以直接执行以下指令来完成安装：

```
sudo apt install tcllib tcl tcl-dev tklib tk tk-dev 
```

## 配置步骤（源码编译）

### TCL

参考 [ [1] ], [ [2] ]

1. 在 https://www.tcl-lang.org 上找到下载链接并下载（具体链接根据实际情况而定）：

    ```
    wget http://prdownloads.sourceforge.net/tcl/tcl9.0.1-src.tar.gz
    ```

    并解压（具体文件名称根据实际情况而定）：

    ```
    tar -xvf tcl9.0.1rc0-src.tar
    ```

    进入目录：

    ```
    cd tcl9.0.1
    ```

2. 新建存放编译结果的目录：

    ```
    mkdir TCL-installed
    ```

3. 进入目录：

    ```
    cd unix
    ```

4. configure：

    ```
    ./configure --prefix=/home/huangcanjia/tcl9.0.1/TCL-installed/
    ```

    这里 `prefix` 设置的是之前新建的存放编译结果的目录的绝对路径

5. 编译：

    ```
    make
    ```

6. 安装：

    ```
    make install
    ```

### TK

过程同 **TCL** 的安装

 - :warning: 需要注意 **TK** 的版本需要和 **TCL** 相匹配，如果之前安装过其他版本的 **TCL**，在进行 configure 的过程中可能会出现错误 `configure: error: tk 8.6 requires Tcl 8.6+`

    此时将之前安装 **TCL** 的目录名称展示更改，再重新进行 configure 即可。如我这里将 “tcl9.0.1” 目录名称暂时改为 “tmp-tcl9.0.1”

[1]: https://zhuanlan.zhihu.com/p/423324052
[2]: https://blog.csdn.net/RadiantJeral/article/details/108021607