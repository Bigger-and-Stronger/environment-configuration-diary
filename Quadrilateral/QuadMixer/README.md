# QuadWild 项目配置记录

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
    abstract = {We propose QuadMixer, a novel interactive technique to compose quad mesh components preserving the majority of the original layouts. Quad Layout is a crucial property for many applications since it conveys important information that would otherwise be destroyed by techniques that aim only at preserving shape.Our technique keeps untouched all the quads in the patches which are not involved in the blending. We first perform robust boolean operations on the corresponding triangle meshes. Then we use this result to identify and build new surface patches for small regions neighboring the intersection curves. These blending patches are carefully quadrangulated respecting boundary constraints and stitched back to the untouched parts of the original models. The resulting mesh preserves the designed edge flow that, by construction, is captured and incorporated to the new quads as much as possible. We present our technique in an interactive tool to show its usability and robustness.},
    journal = {ACM Trans. Graph.},
    month = {nov},
    articleno = {180},
    numpages = {13},
    keywords = {mesh modelling, retopology, quadrangulation}
}
```