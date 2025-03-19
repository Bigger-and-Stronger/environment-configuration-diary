# QuadWild with Bi-MDF solver 项目配置记录

本文档为配置文章 **"Min-Deviation-Flow in Bi-directed Graphs for T-Mesh Quantization"** 的代码的记录 [[Paper]](https://dl.acm.org/doi/10.1145/3592437) [[Project Page]](https://www.algohex.eu/publications/bimdf-quantization/) [[Code]](https://github.com/cgg-bern/quadwild-bimdf)

```
@article{Heistermann:2023:BiMDF,
    author = {Heistermann, Martin and Warnett, Jethro and Bommes, David},
    title = {Min-Deviation-Flow in Bi-directed Graphs for T-Mesh Quantization},
    journal = {ACM Transactions on Graphics},
    volume = {42},
    number = {4},
    year = {2023},
    publisher = {ACM},
    address = {New York, NY, USA},
    doi = {10.1145/3592437}
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 19/3/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.5 LTS
- SSH IDE：CLion 2024.3.4

## 配置步骤

---

:star: 该项目有发布预先编译好的可执行文件，可直接在 [quadwild-bimdf/releases](https://github.com/cgg-bern/quadwild-bimdf/releases) 下载使用，不需要进行以下配置步骤

---

1. 将项目下载到本地，在终端中输入：

    ```
    git clone --recursive https://github.com/cgg-bern/quadwild-bimdf/
    ```

    并进入该项目目录：

    ```
    cd quadwild-bimdf
    ```

2. 按照 [quadwild-bimdf/READMD](https://github.com/cgg-bern/quadwild-bimdf/blob/main/README.md) 中的步骤，执行：

    ```
    cmake . -B build -DSATSUMA_ENABLE_BLOSSOM5=0
    ```

    ```
    cmake --build build
    ```

    - :warning: 可能出现错误 `fatal error: span: No such file or directory`

        `span` 是一个 C++20 的标准头文件，可能是 gcc 的版本太低导致的，可以参考 [[1]](https://blog.csdn.net/qq_38308388/article/details/127574517) 进行安装