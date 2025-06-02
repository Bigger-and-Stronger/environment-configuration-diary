# CGAL 库配置记录

本文档为配置 CGAL 库的记录，[[官网]](https://www.cgal.org)

---

Canjia Huang <<canjia7@gmail.com>> last update 14/4/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.5 LTS

## 配置步骤（无 root）

1. 从 https://github.com/CGAL/cgal/releases 上下载所需要的 Release 版本，如（具体链接根据实际情况而定）：

    ```
    wget https://github.com/CGAL/cgal/releases/download/v5.6.2/CGAL-5.6.2.tar.xz
    ```

2. 解压（具体文件名称根据实际情况而定）：

    ```
    tar -xvf CGAL-5.6.2.tar.xz
    ```

3. 添加环境变量：

    ```
    vim ~/.bashrc
    ```

    在文件的最后添加（具体路径根据实际情况而定）：

    ```
    export CGAL_ROOT=/home/huangcanjia/CGAL-5.6.2/
    ```

    保存并退出，然后重新加载环境变量：

    ```
    source ~/.bashrc
    ```

# 常见错误

- :warning: 如果在项目中使用 **CGAL** 库时出现错误 `error: ‘if_c’ in namespace ‘boost::mpl’ does not name a template type`，这是因为 **CGAL** 所使用的 **Boost** 库的版本过高或过低，需要选择在 1.66.0-1.78.0 之间的版本（ **Boost** 库的配置过程见 [Boost 库配置记录](../Boost/) ）