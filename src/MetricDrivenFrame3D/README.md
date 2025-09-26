# MetricDrivenFrame3D 项目配置记录

本文档为配置文章 **"Metric-Driven 3D Frame Field Generation"** 的代码的记录 [[Paper]](https://ieeexplore.ieee.org/document/9655471) [[exe]](https://github.com/xianzhongfang/MetricDrivenFrame3D)

```
@ARTICLE{9655471,
    author={Fang, Xianzhong and Huang, Jin and Tong, Yiying and Bao, Hujun},
    journal={IEEE Transactions on Visualization and Computer Graphics}, 
    title={Metric-Driven 3D Frame Field Generation}, 
    year={2023},
    volume={29},
    number={4},
    pages={1964-1976},
    keywords={Measurement;Three-dimensional displays;Strain;Visualization;Shape;Tensors;Solid modeling;Frame field;Riemannian metric;covariant derivative;connection},
    doi={10.1109/TVCG.2021.3136199}
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 7/4/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 预备步骤

如果有 root 权限的话，可以执行指令安装所有依赖库：

```
sudo apt install gfortran libalglib-dev libblas-dev libcholmod3 libgomp1 minpack-dev petsc-dev
```

如果没有 root 权限的话，安装过程如下：

1. 安装 **minpack** 库，具体参考 [Minpack 库配置记录](../Minpack/) 和 [CMinpack 库配置记录](../CMinpack/)，需要编译出动态链接库，以及软链接 “libminpack.so.1” 并将链接库目录添加到系统环境变量

    - :star: 软链接的生成方式如：

        ```
        ln -s libminpack.so libminpack.so.1
        ```

    我这里选择的是配置 **CMinpack**，并选择生成动态链接库（默认是静态链接库），然后将 libcminpack.so 软链接到 libminpack.so.1

2. 安装 **alglib** 库，具体参考 [ALGLIB 库配置记录](../ALGLIB/) 需要编译出动态链接库，以及软链接 “libalglib.so.3.14” 并将链接库目录添加到系统环境变量

    我这里选择的是直接通过 deb 安装 alglib3.14，可以直接得到链接库文件 “libalglib.so.3.14”（无需进行软链接）

## 配置步骤

参考 [MetricDrivenFrame3D/README](https://github.com/xianzhongfang/MetricDrivenFrame3D/blob/master/README.md)

1. 将项目下载到本地：

    ```
    git clone https://github.com/xianzhongfang/MetricDrivenFrame3D.git
    ```

    并进入目录：

    ```
    cd MetricDrivenFrame3D
    ```

## 测试

该项目根目录下有脚本 “run.sh”，直接在终端中运行：

```
bash run.sh
```

- :warning: 可能出现错误 `symbol lookup error: /home/huangcanjia/MetricDrivenFrame3D/bin/MetricDrivenFrame3D: undefined symbol: lmder1_`

    该问题是由于 **minpack** 安装得到的链接库有误导致的，请检查安装过程

- :warning: 可能出现错误 `symbol lookup error: /home/huangcanjia/MetricDrivenFrame3D/bin/MetricDrivenFrame3D: undefined symbol: _ZN6alglib15minlbfgssetcondERKNS_13minlbfgsstateEdddlNS_7xparamsE`

    该问题是由于 **alglib** 安装得到的链接库有误导致的，请检查安装过程