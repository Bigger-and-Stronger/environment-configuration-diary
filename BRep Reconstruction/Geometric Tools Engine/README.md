# Geometric Tools Engine与曲面拟合
Shi Chen 24/02/2025 20:51

 *一篇不用怎么配置环境的配环境日记，但或许是有用的。*

## 引言
BRep重建是一个庞大的工程，但幸运的是，目前存在一些基于机器学习的CAD点云分割技术能够为我们创造分块的点云数据。有兴趣请见:
- [另一篇配置日记](https://github.com/Bigger-and-Stronger/environment-configuration-diary/tree/main/BRep%20Reconstruction/ParseNet%2BSED_Net)
- [相关文献整理](https://github.com/Bigger-and-Stronger/awesome-brep-reconstruction)

有了分块点云后，我们的下一步是对每一块进行曲面拟合，之后再对拟合结果求交得到BRep。拟合与求交都是极具挑战性的问题，本文主要介绍的是用于曲面拟合的C++开源库Geometric Tools Engine(GTE)：
- [Website](https://www.geometrictools.com/)
- [Geometric Tools on GitHub](https://github.com/davideberly/GeometricTools)

这个库使用方便且极其强大，以至于许多BRep重建的优秀工作都使用了它，如：
- [ComplexGen](https://github.com/guohaoxiang/ComplexGen)
- [Split and fit](https://github.com/yilinliu77/NVDNet)

本文只涉及GTE中的曲面拟合功能。

## 配置
直接将源码添加到include路径即可，是的**完全没有配置成本！**
git clone或直接下载到本地：
```bash
	git clone https://github.com/davideberly/GeometricTools
```
曲面拟合功能在以下目录：
```bash
	GTE/Mathematics
```
举个栗子，例如你的项目在 *Project* 文件夹下：
```bash
	- Project
		- CMakeLists.txt
		- src
			- /* 这里是源码 */
		- data
			- /* 这里放置测试数据 */
		- lib
			- /* 将Mathematics整个文件夹放在这里 */
			- Mathematics 
```

`CMakeLists.txt` 中应有(这里咱假设项目名就叫`Project`)：
``` bash
	... ...
	project(Project)
	... ...
	... ...
	# GTE
	target_include_directories(Project PRIVATE lib)
	... ...
```

当然，手动添加到include路径也不是不行。

## 曲面拟合例子
这里介绍一些例子，曲面拟合结果存储为[OCCT](https://dev.opencascade.org/)中的数据结构(如`gp_Pnt`为点, `gp_Dir`为方向)，如果不习惯或有其他需求也可使用Eigen中的向量或自定义数据结构存储。
### 球面拟合
```bash
	std::vector<gte::Vector3<double>> gte_data;
    /* 填充gte_data */
    gte::Sphere3<double> gte_sphere;
    gte::ApprSphere3<double> fitter;
	/ * 获得拟合结果, 球半径, 球心 */
    auto result = fitter.FitUsingSquaredLengths(gte_data.size(), gte_data.data(), gte_sphere);
    gp_Pnt center = gp_Pnt(gte_sphere.center[0], gte_sphere.center[1], gte_sphere.center[2]);
    double radius = gte_sphere.radius;
```
### 柱面拟合
```bash
	std::vector<gte::Vector3<double>> gte_data;
	/* 填充gte_data */
    gte::Cylinder3<double> gte_cylinder;
    gte::ApprCylinder3<double> cylinderFitter(20, 2048, 1024);
    cylinderFitter(gte_data.size(), gte_data.data(), gte_cylinder);
	/ * 获得拟合结果, 圆柱半径, 圆心，旋转轴方向 */
    double radius = gte_cylinder.radius;
    gp_Pnt center_cyl(gte_cylinder.axis.origin[0], gte_cylinder.axis.origin[1], gte_cylinder.axis.origin[2]);
    gp_Dir axis_cyl(gte_cylinder.axis.direction[0], gte_cylinder.axis.direction[1], gte_cylinder.axis.direction[2]);
```


## 参考
这里展示的代码参考了[Split and fit](https://github.com/yilinliu77/NVDNet)。

