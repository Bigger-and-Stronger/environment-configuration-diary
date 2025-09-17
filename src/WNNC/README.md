# Winding Number Normal Consistency (WNNC)

*Shi Chen 17/09/2025*


## 论文

Siyou Lin, Zuoqiang Shi, Yebin Liu, *"Fast and Globally Consistent Normal Orientation based on the Winding Number Normal Consistency".* 
- TOG 2024
- [Paper](https://arxiv.org/abs/2405.16634) | [Project Page](https://jsnln.github.io/wnnc/index.html) | [Code](https://github.com/jsnln/WNNC)




**说明：**
- 该论文的工作是快速估计点云法向，为代码中的Python实现部分。
- 本仓库还涉及另一篇点云重建过程，即[PGR](https://jsnln.github.io/tog2022_pgr/index.html)，由C++实现。
- 我们只配置法向估计部分内容。

## 配置过程

- 创建新环境，进入环境，安装torch
```

	conda create -n wnnc_env python=3.8
	conda activate wnnc_env
	conda install pytorch==1.9.1 torchvision==0.10.1 torchaudio==0.9.1 cudatoolkit=11.1 -c pytorch -c nvidia

```

- 克隆仓库
```
	
	git clone https://ghproxy.com/https://github.com/jsnln/WNNC.git
	cd WNNC
```

- 配置`wn_treecode`
```

	cd ext
	pip install -e .
	cd ..

```

- 配置其他依赖，作者没有提供环境文件，但是这个代码的依赖不多，我们手动配置一下吧
```

	pip install tqdm
	pip install psutil
```



## 运行



```
	# width is important for normal quality, we provide a few presets through --width_config
	
	# for clean uniform samples, use l0
	python main_wnnc.py data/Armadillo_40000.xyz --width_config l0 --tqdm
	
	# for noisy or non-uniform points, use configs l1 (small noise) ~ l5 (large noise) depending on the noise level
	# a higher level gives smoother normals and better resilience to noise
	python main_wnnc.py data/bunny_noised.xyz --width_config l1 --tqdm
	...
	python main_wnnc.py data/bunny_noised.xyz --width_config l5 --tqdm
	
	# the user can also use custom widths:
	python main_wnnc.py data/bunny_noised.xyz --width_config custom --wsmin 0.03 --wsmax 0.12 --tqdm
	
	# to see a complete list of options:
	python main_wnnc.py -h


```

输入在`data`文件夹，输出在`result`文件夹，数据格式都是`.xyz`，存储格式如下：

```
	
	# without normal
	
	x y z
	
	# with normal
	
	x y z nx ny nz

```