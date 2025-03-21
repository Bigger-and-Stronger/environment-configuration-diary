# HOHQMesh 项目配置记录

本文档为配置开源项目 **"HOHQMesh: High Order Hex-Quad Mesher"** 的记录 [[Paper]](https://joss.theoj.org/papers/10.21105/joss.07476) [[Gallery]](https://trixi-framework.github.io/HOHQMesh/Gallery/) [[Code]](https://github.com/trixi-framework/HOHQMesh)

```
@article{kopriva2024hohqmesh:joss,
  title={{HOHQM}esh: An All Quadrilateral/Hexahedral Unstructured Mesh Generator for High Order Elements},
  author={David A. Kopriva and Andrew R. Winters and Michael Schlottke-Lakemper
          and Joseph A. Schoonover and Hendrik Ranocha},
  year={2024},
  journal={Journal of Open Source Software},
  doi={10.21105/joss.07476},
  volume = {9},
  number = {104},
  pages = {7476},
  publisher = {The Open Journal}
}
```

```
@misc{kopriva2024hohqmesh:repo,
  title={{HOHQM}esh: An All Quadrilateral/Hexahedral Unstructured Mesh Generator for High Order Elements},
  author={Kopriva, David A and Winters, Andrew R and Schlottke-Lakemper, Michael
          and Schoonover, Joseph A and Ranocha, Hendrik},
  year={2024},
  howpublished={\url{https://github.com/trixi-framework/HOHQMesh}},
  doi={10.5281/zenodo.13959058}
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 21/3/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.5 LTS

---

:star: 该项目于 [HOHQMesh/release](https://github.com/trixi-framework/HOHQMesh/releases/tag/v1.5.4) 中提供了编译好的可执行文件，可以直接使用，不需要以下配置步骤

---

[HOHQMesh/README](https://github.com/trixi-framework/HOHQMesh/blob/main/README.md) 中提供了几种配置方案，实际配置时可以选择更直接的方式，这里选择较为麻烦的源码编译

## 配置步骤 （CMake 源码编译）

1. 将该项目 `git clone` 到本地：

    ```
    git clone https://github.com/trixi-framework/HOHQMesh.git
    ```

    进入项目目录：

    ```
    cd HOHQMesh/
    ```

2. 执行脚本以下载 **FTObjectLibrary** sources，执行：

    ```
    ./Utilities/bootstrap
    ```

3. 参考 [HOHQMesh/README/Using CMake] 编译 **FTObjectLibrary** 库，执行：

    ```
    mkdir build-ftol && cd build-ftol
    cmake ../Contrib/FTObjectLibrary/ -DCMAKE_INSTALL_PREFIX=../install
    cmake --build .
    cmake --install .
    cd ..
    ```

4. 参考 [HOHQMesh/README/Using CMake] 编译 **HOHQMesh** ，执行：

    ```
    mkdir build-hm && cd build-hm
    CMAKE_PREFIX_PATH=../install cmake .. -DCMAKE_INSTALL_PREFIX=../install
    cmake --build .
    cmake --install .
    cd ..
    ```

5. 为了方便使用，将编译得到的可执行文件 "HOHQMesh" 复制到项目根目录：

    ```
    cp install/bin/HOHQMesh .
    ```

## 测试

项目自身提供了一些测试例子

### 2D

在项目根目录执行：

```
./HOHQMesh -f Examples/2D/GingerbreadMan/GingerbreadMan.control
```

执行结束后会在 “Examples/2D/GingerbreadMan” 目录下生成 “.tec”（可以使用 **paraview** 打开）, ".txt", ".mesh" 的结果文件


### 3D

在项目根目录执行：

```
./HOHQMesh -f Examples/3D/BottomFromFile/BottomFromFile.control
```

执行结束后会在 “Examples/3D/BottomFromFile” 目录下生成 “.tec”（可以使用 **paraview** 打开）, ".inp" 结果文件

[HOHQMesh/README/Using CMake]: https://github.com/trixi-framework/HOHQMesh?tab=readme-ov-file#using-cmake