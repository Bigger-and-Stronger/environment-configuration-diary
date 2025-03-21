# QuadMixer 项目配置记录

本文档为配置文章 **"QuadMixer: Layout Preserving Blending of Quadrilateral Meshes"** 的代码的记录 [[Paper]](https://dl.acm.org/doi/10.1145/3355089.3356542) [[Code]](https://github.com/stefanonuvoli/quadmixer)

```
@article{10.1145/3355089.3356542,
    author = {Nuvoli, Stefano and Hernandez, Alex and Esperan\c{c}a, Claudio and Scateni, Riccardo and Cignoni, Paolo and Pietroni, Nico},
    title = {QuadMixer: Layout Preserving Blending of Quadrilateral Meshes},
    year = {2019},
    issue_date = {November 2019},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    volume = {38},
    number = {6},
    issn = {0730-0301},
    url = {https://doi.org/10.1145/3355089.3356542},
    doi = {10.1145/3355089.3356542},
    journal = {ACM Trans. Graph.},
    month = {nov},
    articleno = {180},
    numpages = {13},
    keywords = {mesh modelling, retopology, quadrangulation}
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 21/3/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 预备步骤

- 该项目依赖于 Gurobi 库，安装步骤可参考 [Gurobi 库配置记录](../Gurobi/)
- 该项目还依赖于 eigen, boost, cgal 库

## 配置步骤

1. 将项目下载到本地：

    ```
    git clone --recursive https://github.com/stefanonuvoli/quadmixer
    ```

    进入项目目录：

    ```
    cd quadmixer/
    ```

2. 编辑配置文件：

    ```
    vim configuration.pri
    ```

    需要确认并更改下图红框中的各依赖库的路径和版本信息（根据实际情况调整）：

    ![image](.pic/image.png)

    - 其中 `CGAL_PATH` 路径不能设置为 “/usr/include/CGAL”，而应该设定为该目录的上一级目录
    - 其中 `GUROBI_COMPILER` 和 `GUROBI_LIB` 的设置可以参考 **Gurobi** 库的安装目录 “gurobi1201/linux64/lib/” 下的文件，如我在该目录下存在文件 `libgurobi_g++8.5.a` 和 `libgurobi120.so`，以此来确定我这里填写的参数

    修改完毕后保存退出

3. 新建存放编译文件的目录并进入：

    ```
    mkdir build
    cd build
    ```

4. 使用 **qmake** 进行配置：

    ```
    qmake ../quadmixer.pro
    ```

    配置完成后会在本目录下生成 “Makefile” 文件

5. 编译：

    ```
    make -j8
    ```

    - :warning: 可能出现错误 `fatal error: stdlib.h: No such file or directory`

        参考 [ [1] ] [ [2] ]，可能是因为 gcc 的版本过高导致的

        一种解决方法是去掉配置文件 “configuration.pri” 中包含的 “/usr/include” 路径，如可以把 `CGAL_PATH` 的路径去除：

        ```
        vim ../configuration.pri
        ```

        ![image](.pic/image1.png)

    - :warning: 可能出现错误 `/usr/bin/ld: cannot find -ltbb` 和 `/usr/bin/ld: cannot find -lHalf`

        需要安装 **tbb** 库



[1]: https://blog.csdn.net/Kami_Jiang/article/details/123073899
[2]: https://www.jianshu.com/p/94faa8d32519