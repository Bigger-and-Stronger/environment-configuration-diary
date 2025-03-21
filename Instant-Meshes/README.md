# Instant Meshes 项目配置记录

本文档为配置文章 **"Instant Field-Aligned Meshes"** 的代码的记录 [[Paper]](https://dl.acm.org/doi/10.1145/2816795.2818078) [[Project Page]](https://igl.ethz.ch/projects/instant-meshes/) [[Code]](https://github.com/wjakob/instant-meshes)

```
@article{10.1145/2816795.2818078,
    author = {Jakob, Wenzel and Tarini, Marco and Panozzo, Daniele and Sorkine-Hornung, Olga},
    title = {Instant field-aligned meshes},
    year = {2015},
    issue_date = {November 2015},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    volume = {34},
    number = {6},
    issn = {0730-0301},
    url = {https://doi.org/10.1145/2816795.2818078},
    doi = {10.1145/2816795.2818078},
    month = nov,
    articleno = {189},
    numpages = {15},
    keywords = {N-RoSy, extrinsic smoothing, point cloud, quadrangulation, range scan, remeshing, triangulation}
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 21/3/2025

---

:star: 该项目提供了各个平台上已编译好的可执行文件，见 [instant-meshes/README-Pre-compiled binaries](https://github.com/wjakob/instant-meshes?tab=readme-ov-file#pre-compiled-binaries)，可以直接下载使用，无需以下配置步骤

---

# :apple: macOS

- 操作平台：MacBook Air (Apple M3) macOS 15.3.1

## 配置步骤

参考 [instant-meshes/README](https://github.com/wjakob/instant-meshes/blob/master/README.md)

在终端中输入：

```
git clone --recursive https://github.com/wjakob/instant-meshes
cd instant-meshes
cmake .
make -j 4
```

编译完成后在项目目录下会生成应用程序 “Instant Meshes.app”

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤

参考 [instant-meshes/README](https://github.com/wjakob/instant-meshes/blob/master/README.md)

1. 将项目下载到本地，在终端中输入：

    ```
    git clone --recursive https://github.com/wjakob/instant-meshes
    ```