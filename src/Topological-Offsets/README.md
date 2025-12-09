# Topological Offsets 项目配置记录

本文档为配置文章 **"Topological Offsets"** 的代码的记录 [[doi]](https://dl.acm.org/doi/abs/10.1145/3731157) [[code]](https://github.com/wildmeshing/topological-offsets)

```
@article{10.1145/3731157,
    author = {Zint, Daniel and Chen, Zhouyuan and Zhu, Yifei and Zorin, Denis and Schneider, Teseo and Panozzo, Daniele},
    title = {Topological Offsets},
    year = {2025},
    issue_date = {August 2025},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    volume = {44},
    number = {4},
    issn = {0730-0301},
    url = {https://doi.org/10.1145/3731157},
    doi = {10.1145/3731157},
    journal = {ACM Trans. Graph.},
    month = jul,
    articleno = {144},
    numpages = {19},
    keywords = {offsets, meshing}
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 12/9/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤

1. 将项目下载到本地：

    ```
    git clone https://github.com/wildmeshing/topological-offsets.git
    ```

    进入项目目录：

    ```
    cd topological-offsets/
    ```

2. 新建存放编译结果的目录并进入：

    ```
    mkdir build && cd build
    ```

3. 使用 CMake 进行 configure：

    ```
    cmake -DCMAKE_BUILD_TYPE=Release ..
    ```

4. 编译：

    ```
    make -j
    ```

     - :warning: 可能出现错误 `error: all member functions in class ‘Eigen::ReturnByValue<Derived>::YOU_ARE_TRYING_TO_ACCESS_A_SINGLE_COEFFICIENT_IN_A_SPECIAL_EXPRESSION_WHERE_THAT_IS_NOT_ALLOWED_BECAUSE_THAT_WOULD_BE_INEFFICIENT’ are private [-Werror=ctor-dtor-privacy]`

        可以通过在 configure 过程中添加选项 `-Wno-error=ctor-dtor-privacy` 来禁用该错误，首先需要修改 `topological-offsets/CMakeLists.txt` 的 Line 102 为：
        
        ```
        set_property(TARGET wildmeshing_toolkit PROPERTY COMPILE_WARNING_AS_ERROR  OFF)
        ```
        
        清除编译缓存后重新进行添加了选项的 configure：

        ```
        cmake -DCMAKE_BUILD_TYPE=Release .. -DCMAKE_CXX_FLAGS="-Wno-ctor-dtor-privacy"
        ```

        configure 后重新进行编译

    - :warning: 可能出现错误 `error: ‘assert’ was not declared in this scope` 或 `error: there are no arguments to ‘assert’ that depend on a template parameter, so a declaration of ‘assert’ must be available [-fpermissive]`

        该问题出现在文件 `topological-offsets/build/_deps/fast-envelope-build/include/fastenvelope/AABB.h` 中，可以在该文件的开头添加 `#include <cassert>` 并重新编译

        其余可能出现该问题的文件如下，同样方式修改即可：

        - `topological-offsets/src/wmtk/attribute/internal/AttributeTransactionStack.hxx`
        - `topological-offsets/src/wmtk/attribute/internal/AttributeTransactionStack.hpp`
        - `topological-offsets/build/CPM/fast-envelope/835495c632738e05d9583ed2db1b35507bc798f2/src/FastEnvelope.cpp`
        - `topological-offsets/src/wmtk/function/PerSimplexFunction.hpp`
        - `topological-offsets/src/wmtk/function/utils/AutoDiffUtils.hpp`
        - `topological-offsets/src/wmtk/utils/tetmesh_topology_initialization.cpp`
        - `topological-offsets/src/wmtk/utils/orient.cpp`
        - `topological-offsets/src/wmtk/operations/internal/SplitAlternateFacetOptionData.cpp`
        - `topological-offsets/components/topological_offsets/wmtk/components/topological_offsets/internal/utils/compute_tet_amips.cpp`
        - `topological-offsets/components/topological_offsets/wmtk/components/topological_offsets/internal/utils/compute_edge_length.cpp`

    - :warning: 可能出现错误 `error: ‘all’ is not a member of ‘Eigen’`

        该问题出现在文件 `topological-offsets/src/wmtk/io/MshReader.cpp` 中，参考 [ [1] ]，将该文件中的 `Eigen::all` 替换为 `Eigen::indexing::all`

        类似问题还出现在以下文件中，同样方式修改即可：

        - `topological-offsets/src/wmtk/utils/make_free_sv_mesh.cpp`

## 使用步骤

编译完成后，会在 `build/applications/` 目录下生成 `topological_offsets_app` 的可执行文件，进入该目录下，执行：

```
./topological_offsets_app -j ../../input_data/fertility_topo.json
```

生成成功后会在当前目录下生成一些 `.vtu` 的结果文件，可以使用 ParaView 进行可视化

[1]: https://github.com/UMich-BipedLab/LiDARTag/issues/6