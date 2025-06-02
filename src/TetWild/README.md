# TetWild 项目配置记录

本文档为配置文章 **"Tetrahedral Meshing in the Wild"** 的代码的记录 [[Paper]](https://dl.acm.org/doi/10.1145/3197517.3201353) [[Slides]](https://slides.games-cn.org/pdf/GAMES201858胡译心.pdf) [[Code]](https://github.com/Yixin-Hu/TetWild)

```
@article{Hu:2018:TMW:3197517.3201353,
    author = {Hu, Yixin and Zhou, Qingnan and Gao, Xifeng and Jacobson, Alec and Zorin, Denis and Panozzo, Daniele},
    title = {Tetrahedral Meshing in the Wild},
    journal = {ACM Trans. Graph.},
    issue_date = {August 2018},
    volume = {37},
    number = {4},
    month = jul,
    year = {2018},
    issn = {0730-0301},
    pages = {60:1--60:14},
    articleno = {60},
    numpages = {14},
    url = {http://doi.acm.org/10.1145/3197517.3201353},
    doi = {10.1145/3197517.3201353},
    acmid = {3201353},
    publisher = {ACM},
    address = {New York, NY, USA},
    keywords = {mesh generation, robust geometry processing, tetrahedral meshing},
} 
```

---

Canjia Huang <<canjia7@gmail.com>> last update 25/3/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.5 LTS

## 配置步骤（通过CMake）

参考 [TetWild/README-via CMake](https://github.com/Yixin-Hu/TetWild?tab=readme-ov-file#via-cmake)

1. 将项目下载到本地：

    ```
    git clone https://github.com/Yixin-Hu/TetWild
    ```

    并进入项目目录：

    ```
    cd TetWild
    ```

2. 新建存放编译文件的目录并进入：

    ```
    mkdir build
    cd build
    ```

3. 使用 CMake 进行 configure：

    ```
    cmake ..
    ```

4. 编译：

    ```
    make -j8
    ```

    - :warning: **libigl** 库可能出现错误 `error: there are no arguments to ‘assert’ that depend on a template parameter`

        解决方法参考 [fTetWild 项目配置记录](../fTetWild/)

5. 编译完成后会在 "TetWild/build" 目录下生成可执行文件 “TetWild”

## 测试

1. 将测试模型放置在该目录下，这里使用 [jaw.obj](../QuadWild-Bi-MDF-solver/jaw.obj)

2. 在该目录下输入（具体模型名称根据实际情况而定）：

    ```
    ./TetWild jaw.obj
    ```

3. 执行结束后，会在该目录下生成结果文件 “jaw_.csv”，“jaw_.msh”（结果四面体网格，可用 **Gmsh** 打开），“jaw__sf.obj”（结果四面体网格的表面三角网格）