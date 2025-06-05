# TriWild 项目配置记录

本文档为配置文章 **"TriWild: Robust Triangulation With Curve Constraints"** 的代码的记录 [[Doi]](https://dl.acm.org/doi/10.1145/3306346.3323011) [[Paper]](https://dl.acm.org/doi/pdf/10.1145/3306346.3323011) [[Code]](https://github.com/wildmeshing/TriWild)

```
@article{Hu:2019:TRT:3306346.3323011,
    author = {Hu, Yixin and Schneider, Teseo and Gao, Xifeng and Zhou, Qingnan and Jacobson, Alec and Zorin, Denis and Panozzo, Daniele},
    title = {TriWild: Robust Triangulation with Curve Constraints},
    journal = {ACM Trans. Graph.},
    issue_date = {July 2019},
    volume = {38},
    number = {4},
    month = jul,
    year = {2019},
    issn = {0730-0301},
    pages = {52:1--52:15},
    articleno = {52},
    numpages = {15},
    url = {http://doi.acm.org/10.1145/3306346.3323011},
    doi = {10.1145/3306346.3323011},
    acmid = {3323011},
    publisher = {ACM},
    address = {New York, NY, USA},
    keywords = {curved triangulation, mesh generation, robust geometry processing},
}
```

---

Canjia Huang <<canjia7@gmail.com>> update 5/6/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤（通过CMake）

1. 将项目下载到本地：

    ```
    git clone https://github.com/wildmeshing/TriWild
    ```

    并进入该项目：

    ```
    cd TriWild
    ```

2. 新建存放编译结果的目录：

    ```
    mkdir build
    ```

    并进入：

    ```
    cd build
    ```

3. 使用 CMake 进行 configure：

    ```
    cmake ..
    ```

4. 编译：

    ```
    make -j
    ```

    - :warning: **libigl** 库可能出现错误 `error: there are no arguments to ‘assert’ that depend on a template parameter`

        解决方法参考 [fTetWild 项目配置记录](../fTetWild/)，具体需要修改文件 “TriWild/src/triwild/auto_p_bases.cpp”

    编译完成后会在该目录下生成可执行文件 **TriWild**

## 测试

测试用的数据集可以在 https://drive.google.com/file/d/1yhrJtfCVMahwgPc0pmX0D8GAJgZ9M7v9/view?usp=sharing 下载，论文中的数据可以在 https://drive.google.com/file/d/13xZqYpBz1cV1JaakgkcSO6hSbV9or5V4/view?usp=sharing 下载

这里使用论文中的 figure 1 的数据 [input.obj](input.obj) 进行测试，将该文件放置在 “TriWild/build” 目录下

在 “TriWild/build” 目录下执行：

```
./TriWild --input input.obj
```

执行完毕后会在该目录下生成 “input.obj__linear.msh” 的线性网格文件，可以使用 GMsh 打开