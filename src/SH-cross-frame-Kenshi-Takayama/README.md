# SH-cross-frame (by Kenshi Takayama) 项目配置记录

本文档为配置文章 **"Boundary Aligned Smooth 3D Cross-Frame Field"** 的第三方实现（by [Kenshi Takayama](https://kenshi84.github.io)）代码的记录 [[doi]](https://dl.acm.org/doi/abs/10.1145/2070781.2024177) [[code]](https://kenshi84.github.io/misc/frame3d.zip)

```
@article{10.1145/2070781.2024177,
    author = {Huang, Jin and Tong, Yiying and Wei, Hongyu and Bao, Hujun},
    title = {Boundary aligned smooth 3D cross-frame field},
    year = {2011},
    issue_date = {December 2011},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    volume = {30},
    number = {6},
    issn = {0730-0301},
    url = {https://doi.org/10.1145/2070781.2024177},
    doi = {10.1145/2070781.2024177},
    journal = {ACM Trans. Graph.},
    month = dec,
    pages = {1–8},
    numpages = {8},
    keywords = {spherical harmonics, hexahedral, N-RoSy frame field}
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 25/9/2025

# :penguin: Ubuntu

- 操作系统：macOS Tahoe 26.1

## 配置步骤

1. 将项目代码 [[code]](https://kenshi84.github.io/misc/frame3d.zip) 下载到本地，解压缩，并通过命令行进入项目目录

2. 新建存放编译结果的目录并进入：

    ```
    mkdir build && cd build
    ```

3. 使用 CMake 进行 configure

    ```
    cmake ..
    ```

    - :warning: 可能出现错误 `CMake Error at CMakeLists.txt:2 (CMAKE_MINIMUM_REQUIRED): Compatibility with CMake < 3.5 has been removed from CMake.`

        该问题源于该项目的 CMakeLists.txt 中设置的 CMake 最小版本需求过低，可以通过提高该项目根目录下 CMakeLists.txt 中的 Line 2 中所需求的 CMake 最小版本，如修改为：

        ```
        CMAKE_MINIMUM_REQUIRED(VERSION 3.10)
        ```

        修改完毕后，重新进行 configure

4. 编译：

    ```
    make
    ```