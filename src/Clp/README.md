# COIN_OR Clp 库配置记录

本文档为配置线形规划求解器库 COIN-OR Clp 的记录 [[code]](https://github.com/coin-or/Clp)

---

Canjia Huang <<huangcanjia0214@gmail.com>> last update 24/4/2026

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤

1. 提供了 [coinbrew](https://github.com/coin-or/coinbrew) 脚本用于自动安装

    新建存放目录并进入：
    ```
    mkdir coinbrew && cd coinbrew
    ```
   
2. 下载脚本：
    ```
    wget https://raw.githubusercontent.com/coin-or/coinbrew/master/coinbrew
    ```

    更改脚本权限：
    ```
    chmod u+x coinbrew
    ``` 

3. 执行：
    ```
    ./coinbrew build Cbc@stable/2.10
    ```

    - :warning: 如果出现网络问题导致的下载失败，可以重复执行几次...

4. 安装完毕后，添加相关路径到系统环境变量中：
    ```
    vim ~/.bashrc
    ```

    将以下内容添加到最后（具体路径根据实际情况而定）：
    ```
    export PATH=/home/huangcanjia/coinbrew/dist/bin/:$PATH
    export LD_LIBRARY_PATH=/home/huangcanjia/coinbrew/dist/lib/:$LD_LIBRARY_PATH
    export PKG_CONFIG_PATH=/home/huangcanjia/coinbrew/dist/lib/pkgconfig/:$PKG_CONFIG_PATH
    ```

    保存并退出后，重新加载系统环境变量：
    ```
    source ~/.bashrc
    ```