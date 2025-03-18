# libQEx 项目配置记录

本文档为配置文章 **"QEx: robust quad mesh extraction"** 的代码的记录 [[Paper]](https://dl.acm.org/doi/10.1145/2508363.2508372) [[Code]](https://github.com/hcebke/libQEx)

```
@article{Ebke:2013:QRQ:2508363.2508372,
    author = {Ebke, Hans-Christian and Bommes, David and Campen, Marcel and Kobbelt, Leif},
    title = {{QE}x: Robust Quad Mesh Extraction},
    journal = {ACM Trans. Graph.},
    issue_date = {November 2013},
    volume = {32},
    number = {6},
    month = nov,
    year = {2013},
    issn = {0730-0301},
    pages = {168:1--168:10},
    articleno = {168},
    numpages = {10},
    url = {http://doi.acm.org/10.1145/2508363.2508372},
    doi = {10.1145/2508363.2508372},
    acmid = {2508372},
    publisher = {ACM},
    address = {New York, NY, USA},
    keywords = {integer-grid maps, quad extraction, quad meshing},
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 18/3/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6
- SSH IDE：CLion 2024.3.4

## 配置步骤

1. 将项目下载到本地，在终端中输入：

    ```
    git clone https://github.com/hcebke/libQEx.git
    ```

    并进入该项目目录：

    ```
    cd libQEx
    ```

2. 在该项目根目录处新建目录 `build`，并进入该目录：

    ```
    mkdir build
    cd build
    ```

3. 使用 CMake 进行生成：

    ```
    cmake ..
    ```

    - :warning: 可能出现错误 `Could NOT find OpenMesh (missing: OPENMESH_CORE_LIBRARY`

        需要安装 **OpenMesh** 库，具体可以参考 [Bigger-and-Stronger/environment-configuration-diary/OpenMesh](../../Other-Libraries/OpenMesh)