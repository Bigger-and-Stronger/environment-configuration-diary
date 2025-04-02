# fTetWild 项目配置记录

本文档为配置文章 **"Fast Tetrahedral Meshing in the Wild"** 的代码的记录 [[Paper]](https://dl.acm.org/doi/abs/10.1145/3386569.3392385) [[Code]](https://github.com/wildmeshing/fTetWild)

```
@article{10.1145/3386569.3392385,
    author = {Hu, Yixin and Schneider, Teseo and Wang, Bolun and Zorin, Denis and Panozzo, Daniele},
    title = {Fast Tetrahedral Meshing in the Wild},
    year = {2020},
    issue_date = {July 2020},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    volume = {39},
    number = {4},
    issn = {0730-0301},
    url = {https://doi.org/10.1145/3386569.3392385},
    doi = {10.1145/3386569.3392385},
    journal = {ACM Trans. Graph.},
    month = jul,
    articleno = {117},
    numpages = {18},
    keywords = {mesh generation, robust geometry processing, tetrahedral meshing}
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 2/4/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤

参考 [fTetWild/README-installation via CMake](https://github.com/wildmeshing/fTetWild?tab=readme-ov-file#installation-via-cmake)

1. 将项目下载到本地：

    ```
    git clone https://github.com/wildmeshing/fTetWild.git
    ```

    并进入项目目录：

    ```
    cd fTetWild
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

    - :warning: 可能出现错误 `error: ‘assert’ was not declared in this scope`

        解决方法是找到出错的文件，如我这里出错的文件为 “fTetWild/3rdparty/libigl/include/igl/vertex_components.cpp”

        在出错的文件的开头处添加头文件：

        ```
        #include <cassert>
        ```
    
    - :warning: 文件 “fTetWild/src/main.cpp” 可能出现错误 `error: template argument 1 is invalid`

        解决方法是在该文件的 Line 332-333 中的 `Vector3` 改为 `Vector3d`，并且和 `Vector3i` 前添加命名空间 `Eigen`，即改为：

        ```
        std::vector<Eigen::Vector3d> input_vertices;
        std::vector<Eigen::Vector3i> input_faces;
        ```

5. 编译完成后在该文件夹下会出现可执行文件 “FloatTetWild_bin”

## 测试

进入 “fTetWild/build/” 目录下

1. 将测试模型放置在该目录下，这里使用 [jaw.obj](../QuadWild-Bi-MDF-solver/jaw.obj)

2. 输入：

    ```
    ./FloatTetwild_bin -i jaw.obj
    ```

3. 生成结束后会在该目录下生成结果文件 “jaw.obj_.csv”, "jaw.obj_.msh", "jaw.obj__sf.obj", "jaw.obj__tracked_surface.stl"