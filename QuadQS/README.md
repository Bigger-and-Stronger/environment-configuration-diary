# QuadQS 项目配置记录

本文档为配置文章 **"Quasi-structured quadrilateral meshing in Gmsh - a robust pipeline for complex CAD models"** 项目的记录，该文章相关内容可以在作者主页 [[Maxence Reberol]](https://mxncr.github.io) 找到，该项目已经嵌入在 **Gmsh** 中

Canjia Huang <<canjia7@gmail.com>> last update 18/4/2025

## :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.5 LTS

### 预备步骤

该项目嵌入在 **Gmsh** 项目中，可以参考 [Gmsh 库配置记录](../Gmsh/) 进行配置

- :star: 如果需要对 `stp` 等格式进行处理的话，需要配置基于 **OCCT** 的 **Gmsh** 库（关于 **OCCT** 库的配置可以参考 [Open CASCADE Technology 7.5.0 安装](../OCCT/)）

### 测试

进入存放有 **gmsh** 可执行文件的目录下：

```
./gmsh -algo quadqs -2 xxx
```