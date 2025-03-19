# QuadWild 项目配置记录

本文档为配置文章 **"Reliable Feature-Line Driven Quad-Remeshing"** 的代码的记录 [[Paper]](https://dl.acm.org/doi/10.1145/3450626.3459941) [[Project Page]](https://www.quadmesh.cloud) [[Code]](https://github.com/nicopietroni/quadwild)

```
@article{10.1145/3450626.3459941,
    author = {Pietroni, Nico and Nuvoli, Stefano and Alderighi, Thomas and Cignoni, Paolo and Tarini, Marco},
    title = {Reliable Feature-Line Driven Quad-Remeshing},
    year = {2021},
    issue_date = {August 2021},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    volume = {40},
    number = {4},
    issn = {0730-0301},
    url = {https://doi.org/10.1145/3450626.3459941},
    doi = {10.1145/3450626.3459941},
    abstract = {We present a new algorithm for the semi-regular quadrangulation of an input surface, driven by its line features, such as sharp creases. We define a perfectly feature-aligned cross-field and a coarse layout of polygonal-shaped patches where we strictly ensure that all the feature-lines are represented as patch boundaries. To be able to consistently do so, we allow non-quadrilateral patches and T-junctions in the layout; the key is the ability to constrain the layout so that it still admits a globally consistent, T-junction-free, and pure-quad internal tessellation of its patches. This requires the insertion of additional irregular-vertices inside patches, but the regularity of the final-mesh is safeguarded by optimizing for both their number and for their reciprocal alignment. In total, our method guarantees the reproduction of feature-lines by construction, while still producing good quality, isometric, pure-quad, conforming meshes, making it an ideal candidate for CAD models. Moreover, the method is fully automatic, requiring no user intervention, and remarkably reliable, requiring little assumptions on the input mesh, as we demonstrate by batch processing the entire Thingi10K repository, with less than 0.5% of the attempted cases failing to produce a usable mesh.},
    journal = {ACM Trans. Graph.},
    month = {jul},
    articleno = {155},
    numpages = {17},
    keywords = {geometry processing, quad-meshing, modelling}
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 19/3/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.5 LTS
- SSH IDE：CLion 2024.3.4

## 预备步骤

- 该项目依赖于 Gurobi 库，安装步骤可参考 [Gurobi 库配置记录](../../Other-Libraries/Gurobi/)

## 配置步骤

1. 将项目下载到本地，在终端中输入：

    ```
    git clone --recursive https://github.com/nicopietroni/quadwild
    ```

    并进入该项目目录：

    ```
    cd quadwild
    ```