# SH-cross-frame 项目配置记录

本文档为配置文章 **"All-hex meshing using closed-form induced polycube"** 的代码的记录 [[doi]](https://dl.acm.org/doi/abs/10.1145/2897824.2925957) [[code/exe]](http://www.cad.zju.edu.cn/home/hj/16/closed-form-polycube/closed-form-polycube-release-V1.0.7z)

```
@article{10.1145/2897824.2925957,
    author = {Fang, Xianzhong and Xu, Weiwei and Bao, Hujun and Huang, Jin},
    title = {All-hex meshing using closed-form induced polycube},
    year = {2016},
    issue_date = {July 2016},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    volume = {35},
    number = {4},
    issn = {0730-0301},
    url = {https://doi.org/10.1145/2897824.2925957},
    doi = {10.1145/2897824.2925957},
    journal = {ACM Trans. Graph.},
    month = jul,
    articleno = {124},
    numpages = {9},
    keywords = {automatic hexahedral meshing, frame field, polycube map, volumetric parametrization}
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 26/9/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤

1. 将项目下载到本地：

    ```
    wget http://www.cad.zju.edu.cn/home/hj/16/closed-form-polycube/closed-form-polycube-release-V1.0.7z
    ```

    并解压，或在其他设备中解压后再上传目录至服务器

    进入目录：

    ```
    cd closed-form-polycube-release-V1.0/
    ```

2. 参考 "doc/readme.txt"，进入 "bin" 目录：

    ```
    cd bin
    ```
   
   运行该目录下的测试脚本：

    ```
    ./test.sh
    ```

    - :warning: 可能出现错误 `make: ../sys/libc.so.6: version `GLIBC_2.27' not found (required by make)`

        参考 [hybrid-quad 项目配置记录](../hybrid-quad/) 中的解决方案，用系统中的已有的这些链接库来替换所提供的链接库：

        ```
        cp /lib/x86_64-linux-gnu/libc.so.6 ../sys/libc.so.6
        ```

        类似问题可类似方法解决

    - :warning: 可能出现错误 `line 31: 2299637 Segmentation fault`

        待解决