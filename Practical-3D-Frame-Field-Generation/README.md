# Practical-3D-frame-field-generation 项目配置记录

本文档为配置文章 **"Practical 3D frame field generation"** 的代码的记录 [[Doi]](https://dl.acm.org/doi/10.1145/2980179.2982408) [[Supplemental materials (code)]](https://dl.acm.org/doi/suppl/10.1145/2980179.2982408/suppl_file/233-0220.zip)

```
@article{10.1145/2980179.2982408,
    author = {Ray, Nicolas and Sokolov, Dmitry and L\'{e}vy, Bruno},
    title = {Practical 3D frame field generation},
    year = {2016},
    issue_date = {November 2016},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    volume = {35},
    number = {6},
    issn = {0730-0301},
    url = {https://doi.org/10.1145/2980179.2982408},
    doi = {10.1145/2980179.2982408},
    journal = {ACM Trans. Graph.},
    month = dec,
    articleno = {233},
    numpages = {9},
    keywords = {remeshing, smooth frame fields}
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 9/4/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤

1. 将该论文的附加材料下载到本地，并解压：

    ```
    unzip 233-0220.zip -d Practical-3D-frame-field-generation
    ```

    并进入项目目录：

    ```
    cd Practical-3D-frame-field-generation/src
    ```

    文件 “ReadMe.txt” 中写着具体的使用说明

2. 编译：

    ```
    make
    ```

    编译完成后会在该目录下生成可执行文件 `main`

## 测试

在 “Practical-3D-frame-field-generation/src” 目录下执行：

```
./main join.tet
```

执行后会在该目录下生成 “out.obj” 和 “out.txt” 文件