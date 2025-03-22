# MCS Windows11 环境配置
Shi Chen 
22/03/2025 12:16

本文涉及的论文如下：
- Andrea Tagliasacchi, Ibraheem Alhashim, Matt Olson, Hao Zhang. *"Mean Curvature Skeletons"*. 
  - SGP 2012 
  - [[Paper](https://projet.liris.cnrs.fr/imagine/pub/proceedings/SGP-2012/pdf/v31i5pp1735-1744.pdf)][[Code](https://github.com/taiya/starlab-mcfskel)][[CGAL Document](https://doc.cgal.org/latest/Surface_mesh_skeletonization/index.html)]

该论文是骨架抽取的经典工作 :star2:。由于作者提供的可执行文件非常用户友好，且代码已集成到[CGAL](https://www.cgal.org/)。我们不再配置原始代码环境，而是介绍这两种使用方式。

## 可执行文件
[代码仓库](https://github.com/taiya/starlab-mcfskel) 中有可执行文件 :dizzy:，可直接下载。

启动`starlab.exe`后，导入网格。

先生成中轴点:
Filters - Voronoi based MAT - Apply

骨架化:
Filters - MCF Skeletonization - Apply

## CGAL代码示例
目前已集成到CGAL中 :sparkles:，这里介绍在CGAL中的使用方式。

CGAL在Windows 11中的配置教程很多，这里不多介绍，一种比较便捷的方式是用[vcpkg](https://github.com/microsoft/vcpkg)直接安装。

以下是一个实例，将`inputObj`中读取的网格骨架化，导出到`outpuObj`。
```cpp
#include <iostream>
#include <fstream>
#include <filesystem>

#include <map>
#include <vector>
#include <CGAL/Exact_predicates_inexact_constructions_kernel.h>
#include <CGAL/Surface_mesh.h>
#include <CGAL/Mean_curvature_flow_skeletonization.h>
#include <Eigen/Core>
#include <boost/graph/graph_traits.hpp>  

typedef CGAL::Exact_predicates_inexact_constructions_kernel Kernel;
typedef Kernel::Point_3 Point;
typedef CGAL::Surface_mesh<Point> SurfaceMesh;
typedef CGAL::Mean_curvature_flow_skeletonization<SurfaceMesh> Skeletonization;
typedef Skeletonization::Skeleton Skeleton;
typedef boost::graph_traits<Skeleton>::vertex_descriptor SkeletonVertex;
typedef boost::graph_traits<Skeleton>::edge_descriptor SkeletonEdge;

void readMeshObjAndWriteSkeletonObj(const std::string& inputObj, const std::string& outputObj) 
{
    // 读取 OBJ 文件
    SurfaceMesh mesh;
    if (!CGAL::IO::read_OBJ(inputObj, mesh) || mesh.is_empty()) {
        throw std::runtime_error("Failed to read OBJ file or the file is empty.");
    }

    // 执行骨架化
    Skeleton skeleton;
    Skeletonization skeletonizer(mesh);
    skeletonizer.contract_until_convergence();
    skeletonizer.convert_to_skeleton(skeleton);

    // 映射骨架顶点到索引
    std::map<SkeletonVertex, int> vertexIndex;
    std::vector<Eigen::Vector3d> nodes;
    std::vector<std::pair<int, int>> edges;
    int index = 0;

    // 遍历骨架顶点
    for (auto v : boost::make_iterator_range(boost::vertices(skeleton))) {
        Point p = skeleton[v].point;
        nodes.emplace_back(p.x(), p.y(), p.z());
        vertexIndex[v] = index++;
    }

    // 遍历骨架边
    for (auto e : boost::make_iterator_range(boost::edges(skeleton))) {
        SkeletonVertex src = source(e, skeleton);
        SkeletonVertex tgt = target(e, skeleton);
        edges.emplace_back(vertexIndex[src], vertexIndex[tgt]);
    }

    // 写入骨架到 OBJ 文件
    std::ofstream outFile(outputObj);
    if (!outFile.is_open()) {
        throw std::runtime_error("Failed to open output OBJ file: " + outputObj);
    }
    
    for (const auto& node : nodes) {
        outFile << "v " << node.x() << " " << node.y() << " " << node.z() << "\n";
    }

    for (const auto& edge : edges) {
        outFile << "l " << edge.first + 1 << " " << edge.second + 1 << "\n"; // OBJ 索引从 1 开始
    }

    outFile.close();
    std::cout << "Skeleton written to " << outputObj << " successfully!" << std::endl;
}