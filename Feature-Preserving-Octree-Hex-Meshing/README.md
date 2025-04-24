# Feature-Preserving-Octree-Hex-Meshing 项目配置记录

本文档为配置文章 **"Feature preserving octree‐based hexahedral meshing"** 的代码的记录 [[Paper]](https://onlinelibrary.wiley.com/doi/abs/10.1111/cgf.13795) [[Code]](https://github.com/gaoxifeng/Feature-Preserving-Octree-Hex-Meshing)

```
@inproceedings{gao2019feature,
    title={Feature preserving octree-based hexahedral meshing},
    author={Gao, Xifeng and Shen, Hanxiao and Panozzo, Daniele},
    booktitle={Computer graphics forum},
    volume={38},
    number={5},
    pages={135--149},
    year={2019},
    organization={Wiley Online Library}
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 23/4/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤

1. 将项目下载到本地：

    ```
    git clone https://github.com/gaoxifeng/Feature-Preserving-Octree-Hex-Meshing.git
    ```

    并进入项目：

    ```
    cd Feature-Preserving-Octree-Hex-Meshing
    ```

2. 新建存放编译文件的目录：

    ```
    mkdir build
    ```

    并进入该目录：

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

    - :warning: 可能出现错误 `error: could not convert ‘_mm_shuffle_epi32(a, ((((i3 << 6) | (i2 << 4)) | (i1 << 2)) | i0))’ from ‘__m128i’ to ‘const vboolf4’ {aka ‘const embree::vboolf<4>’}`

        该问题是 **libigl** 库中启用了 **Embree** 库所导致的，一种解决方法是不使用该库，可以通过调整 “Feature-Preserving-Octree-Hex-Meshing/CMakeLists.txt” 文件中 Line 78 的选项 `LIBIGL_WITH_EMBREE` 为 `OFF`：

        ```
        option(LIBIGL_WITH_EMBREE      "Use Embree"         OFF)
        ```

        同时还需要将项目中使用到 **Embree** 库的部分注释掉，即注释掉 “Feature-Preserving-Octree-Hex-Meshing/global_functions.cpp” 文件的 Line 5 和 Line 1119

## 测试

编译成功后在 build 目录下会有可执行文件 **RobustPureHexMeshing**

将测试模型放置在该目录下，如这里使用的是 [cow.obj](cow.obj)

在该目录下在终端中执行：

```
./RobustPureHexMeshing --ch GRID --in cow.obj --out output_mesh.mesh
```

执行成功后会在该目录下生成结果文件 “output_mesh.mesh”，“output_mesh.vtk”,“output_mesh_subB.mesh”，“output_mesh_subB.vtk”