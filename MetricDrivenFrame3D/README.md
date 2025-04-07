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

1. 安装 **minpack** 库

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