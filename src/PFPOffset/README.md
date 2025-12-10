# PFPOffset 项目配置记录

本文档为配置文章 **"A Parallel Feature-preserving Mesh Variable Offsetting Method with Dynamic Programming"** 的代码的记录 [[doi]](https://arxiv.org/abs/2310.08997) [[code]](https://github.com/iGame-Lab/PFPOffset?tab=readme-ov-file)

```
@misc{cao2023parallelfeaturepreservingmeshvariable,
      title={A Parallel Feature-preserving Mesh Variable Offsetting Method with Dynamic Programming}, 
      author={Hongyi Cao and Gang Xu and Renshu Gu and Jinlan Xu and Xiaoyu Zhang and Timon Rabczuk},
      year={2023},
      eprint={2310.08997},
      archivePrefix={arXiv},
      primaryClass={cs.GR},
      url={https://arxiv.org/abs/2310.08997}, 
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 12/9/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤

参考 [readme](https://github.com/iGame-Lab/PFPOffset/blob/main/readme.md)


1. 安装 osqp
      1.1. 在用户根目录下，将 osqp 下载到本地：
      ```
      git clone --recursive https://github.com/osqp/osqp
      ```
      并进入该目录：
      ```
      cd osqp
      ```

      1.2 新建存放安装结果的目录（如果有 root 权限，可以跳过该步）：
      ```
      mkdir osqp-installed
      ```

      1.3 新建存放编译结果的目录并进入：
      ```
      mkdir build && cd build
      ```

      1.4 使用 CMake 进行 configure，并设置安装路径为先前创建的目录，具体路径根据实际情况而定（如果有 root 权限，可以不用设置）：
      ```
      cmake -DCMAKE_INSTALL_PREFIX=/home/huangcanjia/osqp/osqp-installed .. -DBUILD_SHARED_LIBS=ON
      ```

      1.5 编译：
      ```
      make -j
      ```

      1.6 安装：
      ```
      make install
      ```

2. 安装 osqp-eigen
      2.1 在用户根目录下，将 osqp-eigen 下载到本地：
      ```
      git clone https://github.com/robotology/osqp-eigen.git
      ```
      并进入该目录：
      ```
      cd osqp-eigen
      ```

      2.2 新建存放安装结果的目录（如果有 root 权限，可以跳过该步）：
      ```
      mkdir osqp-eigen-installed
      ```

      2.3 新建存放编译结果的目录并进入：
      ```
      mkdir build && cd build
      ```

      2.4 使用 CMake 进行 configure，并设置安装路径为先前创建的目录，具体路径根据实际情况而定（如果有 root 权限，可以不用设置），同时还需设置上一步中 osqp 的安装路径至 `CMAKE_PREFIX_PATH` 变量中，具体根据实际情况而定：
      ```
      cmake -DCMAKE_PREFIX_PATH=/home/huangcanjia/osqp/osqp-installed -DCMAKE_INSTALL_PREFIX:PATH=/home/huangcanjia/osqp-eigen/osqp-eigen-installed ..
      ```

      2.5 编译：
      ```
      make -j
      ```

      2.6 安装：
      ```
      make install
      ```

3. 在用户根目录下，将项目下载到本地：
      ```
      git clone https://github.com/iGame-Lab/PFPOffset.git
      ```
      并进入该项目目录：
      ```
      cd PFPOffset
      ```

4. 编译 TetWild
      4.1 在 PFPOffset 目录下，进入 TetWild 目录：
      ```
      cd TetWild
      ```

      4.2 新建存放编译结果的目录并进入：
      ```
      mkdir build && cd build
      ```

      4.3 使用 CMake 进行 configure：
      ```
      cmake .. -DCMAKE_BUILD_TYPE=Release
      ```

      4.4 编译：
      ```
      make -j
      ```

      - :warning: 可能出现错误 `error: there are no arguments to ‘assert’ that depend on a template parameter, so a declaration of ‘assert’ must be available [-fpermissive]` 或 `error: ‘assert’ was not declared in this scope`

            该问题出现在 `PFPOffset/TetWild/extern/libigl/include/igl/mat_max.cpp` 等文件中，在这些出问题的文件开头添加头文件 `#include <cassert>` 并重新编译即可

            其余出现该问题的文件为：
            - `PFPOffset/TetWild/extern/libigl/include/igl/mat_min.cpp`

5. 编译 fTetWild
      5.1 在 PFPOffset 目录下，进入 fTetWild 目录：
      ```
      cd fTetWild
      ```

      5.2 新建存放编译结果的目录并进入：
      ```
      mkdir build && cd build
      ```

      5.3 使用 CMake 进行 configure：
      ```
      cmake .. -DCMAKE_BUILD_TYPE=Release
      ```

      5.4 编译：
      ```
      make -j
      ```

      - :warning: 可能出现错误 `error: there are no arguments to ‘assert’ that depend on a template parameter, so a declaration of ‘assert’ must be available [-fpermissive]` 或 `error: ‘assert’ was not declared in this scope`

            同上，出现该问题的文件如下，在这些文件的开头添加头文件`#include <cassert>` 并重新编译即可：
            - `PFPOffset/fTetWild/3rdparty/libigl/include/igl/vertex_components.cpp`

      - :warning: 可能出现错误 `error: template argument 1 is invalid`

            该问题出现在 `PFPOffset/fTetWild/src/main.cpp` 文件中，解决方法是将该文件的 Line 332-333 中的 `Vector3` 改为 `Eigen::Vector3d`，`Vector3i` 改为 `Eigen::Vector3i`

6. 编译 PFPOffset
      6.1 在 PFPOffset 目录下，新建存放编译结果的目录并进入：
      ```
      mkdir build && cd build
      ```

      6.2 使用 CMake 进行 configure：
      ```
      cmake .. -DCMAKE_BUILD_TYPE=Release
      ```

      - :warning: 可能出现错误 `Could not find a package configuration file provided by "OsqpEigen" with any of the following names`

            可以在 CMake 时指定 `CMAKE_MODULE_PATH` 为先前安装 osqp 和 osqp-eigen 的目录（具体路径根据实际情况而定）：
            ```
            cmake -DCMAKE_PREFIX_PATH=/home/huangcanjia/osqp-eigen/osqp-eigen-installed -DCMAKE_PREFIX_PATH=/home/huangcanjia/osqp/osqp-installed .. -DCMAKE_BUILD_TYPE=Release
            ```

      6.3 编译：
      ```
      make -j
      ```

## 测试步骤

编译成功后，在 `PFPOffset/build` 目录下有可执行文件 `PFPOffset`

可以将需要测试的模型复制到该目录下，如这里使用 [fandisk.obj](./fandisk.obj)，然后在该目录下输入：
```
./PFPOffset  -f fandisk.obj -i=1 -t=8  -d=0.05
```

生成完毕后会在该目录下生成许多结果文件