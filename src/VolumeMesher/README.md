# VolumeMesher 项目配置文档

本文档为配置文章 **"Convex Polyhedral Meshing for Robust Solid Modeling"** 的代码的记录 [[Doi]](http://arxiv.org/abs/2109.14434) [[Code]](https://github.com/MarcoAttene/VolumeMesher)

```
@article{volmesh2021,
  title   = {Convex Polyhedral Meshing for Robust Solid Modeling},
  author  = {Diazzi, Lorenzo and Attene, Marco},
  journal = {ACM Transactions on Graphics (SIGGRAPH Asia 2021)},
  year    = {2021},
  volume  = {40},
  number  = {6}
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 25/6/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤

参考 https://github.com/MarcoAttene/VolumeMesher/blob/master/README.md

1. 将项目下载到本地：

    ```
    git clone https://github.com/MarcoAttene/VolumeMesher
    ```

    并进入项目目录：

    ```
    cd VolumeMesher
    ```

2. 新建存放编译结果的目录：

    ```
    mkdir build
    ```

    进入该目录：

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

## 测试

进入存放编译结果的目录 “build”，执行：

```
./mesh_generator ../models/wood_fish.off
```

生成成功后会在 “build” 目录下生成结果文件 “volume.msh”