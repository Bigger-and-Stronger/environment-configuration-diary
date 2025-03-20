# Gurobi 库配置记录

本文档为配置 Gurobi 库的记录，[[官网]](https://www.gurobi.com) [[中文官网]](http://www.gurobi.cn//)

---

Canjia Huang <<canjia7@gmail.com>> last update 20/3/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS
- Gurobi 版本：12.0.1

## 配置步骤

参考 [ [1] ]

1. 申请许可，按照 [Gurobi/学术申请](http://www.gurobi.cn//NewsView1.Asp?id=4) 中的步骤发送邮件进行申请
2. 收到回复邮件后，该邮件中会包含详细的安装步骤，也可以参考 [Getting Started with Gurobi Optimizer](https://support.gurobi.com/hc/en-us/articles/14799677517585-Getting-Started-with-Gurobi-Optimizer)

    这里首先在 [gurobi/downloads](https://www.gurobi.com/downloads/gurobi-software/) 中下载所需平台的 **Gurobi Optimizer** 版本，这里我下载的是 “gurobi12.0.1_linux64.tar.gz” 版本，可在终端中输入（具体下载链接根据实际情况而定）：

    ```
    wget https://packages.gurobi.com/12.0/gurobi12.0.1_linux64.tar.gz
    ```

    下载完成后解压，执行（具体文件名称根据实际情况而定）：

    ```
    tar -xzvf gurobi12.0.1_linux64.tar.gz
    ```

    解压完成后会出现 “gurobi1201” 目录（具体目录名称依据实际情况而定）

3. 进入解压得到的文件目录中的 “bin” 目录下，在终端中执行（具体路径根据 实际情况/安装版本 而定）：

    ```
    cd gurobi1201/linux64/bin
    ```

    进行激活，在终端中输入(此处的 “xxx“ 需要替换为收到的邮件中给的激活码)：

    ```
    grbgetkey xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    ```

    激活过程中会提示 `In which directory would you like to store the Gurobi license file?` 以选择要把激活得到的配置文件存放在什么地方，这里我选择存放在 “/home/huangcanjia/gurobi1201/”（具体路径根据实际情况而定）

    激活结束后，在该输入目录下会生成 “/home/huangcanjia/gurobi1201/gurobi.lic” 文件

4. 修改环境变量，打开 “~/.bashrc” 文件，在终端中输入：

    ```
    vim ~/.bashrc
    ```

    在 “～/.bashrc” 文件的最后添加（具体路径根据实际情况而定）：

    ```
    export GUROBI_HOME="/home/huangcanjia/gurobi1201/linux64"
    export PATH="${PATH}:${GUROBI_HOME}/bin"
    export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:${GUROBI_HOME}/lib"
    export GRB_LICENSE_FILE="/home/huangcanjia/gurobi1201/gurobi.lic"
    ```

    保存退出后，在终端中执行：

    ```
    source ~/.bashrc
    ```

5. 编译（可选）

    5.1.  如果需要在 python 中使用该库，还需要在 python 环境中进行安装，[ [1] ] 中提到的 `python setup.py install` 安装方式已经被移除，不再可用
    
    可以参考 [How do I install Gurobi for Python?](https://support.gurobi.com/hc/en-us/articles/360044290292-How-do-I-install-Gurobi-for-Python) 进行安装

    如可在终端中执行：

    ```
    python -m pip install gurobipy
    ```
    
    5.2. 如果需要在 C++ 中使用该库，参考 [ [2] ] 编译链接库，进入目录 “/home/huangcanjia/gurobi1201/linux64/src/build/”：

    ```
    cd gurobi1201/linux64/src/build
    ```

    该文件夹下有 **Makefile** 文件，进行编译：

    ```
    make -j8
    ```

    编译成功后会生成 **libgurobi_c++.a** 文件，将其复制到 "gurobi1201/linux64/lib/" 目录下：

    ```
    cp libgurobi_c++.a ../../lib/
    ```

[1]: https://zhuanlan.zhihu.com/p/79524375
[2]: https://blog.csdn.net/tuck_frump/article/details/130991493