# pythonocc 安装

*Xiaoyang Yu, 2025-06-02.*

### :penguin: Ubuntu

平台：Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-125-generic x86_64)

---

这是有关配置 python 版本 OCC 的记录，此时 OCC 的最新版本是7.9.0版本。参考资料：

[项目仓库](https://github.com/tpaviot/pythonocc-core)


### 配置

pythonocc 提供了预编译的 conda 软件包。参考项目仓库给出的配置方法：


        $ conda create --name=pyoccenv python=3.10
        $ conda activate pyoccenv
        $ conda install -c conda-forge pythonocc-core=7.9.0

到此 pythonocc 安装结束，十分顺畅。

### 测试

我这里给出了一个测试文件，运行 `python create_cube.py` 测试程序，如果安装成功，会导出一个 `cube.step` 文件，并且出现一个可视化窗口。如果是在服务器上运行程序且不支持可视化，请注释 `display_shape(cube)`。