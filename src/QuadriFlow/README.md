# QuadriFlow 项目配置记录

本文档为配置文章 **"QuadriFlow: A Scalable and Robust Method for Quadrangulation"** 的代码的记录 [[Paper]](https://onlinelibrary.wiley.com/doi/abs/10.1111/cgf.13498) [[Code]](https://github.com/hjwdzh/QuadriFlow)

```
@article {10.1111:cgf.13498,
    journal = {Computer Graphics Forum},
    title = {{QuadriFlow: A Scalable and Robust Method for Quadrangulation}},
    author = {Huang, Jingwei and Zhou, Yichao and Niessner, Matthias and Shewchuk, Jonathan Richard and Guibas, Leonidas J.},
    year = {2018},
    publisher = {The Eurographics Association and John Wiley & Sons Ltd.},
    ISSN = {1467-8659},
    DOI = {10.1111/cgf.13498}
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 24/3/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.5 LTS

---

:star: 该项目提供了在线的网格生成工具，可以参考 [Compare](https://yichaozhou.com/publication/1805quadriflow/#demo) 和 [Quadrangulate](https://yichaozhou.com/publication/1805quadriflow/#tool) 进行使用，而无需以下配置过程

---

## 配置步骤

参考 [QuadriFlow/README](https://github.com/hjwdzh/QuadriFlow/blob/master/README.md)

1. 将项目下载到本地：

    ```
    git clone https://github.com/hjwdzh/QuadriFlow.git
    ```

    进入项目目录：

    ```
    cd QuadriFlow
    ```

2. 新建构建结果文件夹并进入：

    ```
    mkdir build
    cd build
    ```

3. 使用 CMake 进行 configure：

    ```
    cmake .. -DCMAKE_BUILD_TYPE=release
    ```

4. 编译：

    ```
    make -j
    ```

5. 编译完成后会在 "QuadriFlow/build" 目录下生成可执行文件 “quadriflow”

## 测试

参考 [QuadriFlow/README](https://github.com/hjwdzh/QuadriFlow/blob/master/README.md)

1. 将测试模型放置在该目录下，这里使用 [jaw.obj](../QuadWild-Bi-MDF-solver/jaw.obj)

2. 在该目录下输入：

    ```
    ./quadriflow -i jaw.obj -o output.obj -f 10000
    ```