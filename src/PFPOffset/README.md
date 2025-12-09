# PFPOffset 项目配置记录

本文档为配置文章 **"A Parallel Feature-preserving Mesh Variable Offsetting Method with Dynamic Programming"** 的代码的记录 [[doi]](https://arxiv.org/abs/2310.08997) [[code]](https://github.com/iGame-Lab/PFPOffset?tab=readme-ov-file)

```
@misc{cao2023parallelfeaturepreservingmeshvariable,
      title={A Parallel Feature-preserving Mesh Variable Offsetting Method with Dynamic Programming}, 
      author={Hongyi Cao and Gang Xu and Renshu Gu and Jinlan Xu and Xiaoyu Zhang and Timon Rabczuk},
      year={2023},
      eprint={2310.08997},
      archivePrefix={arXiv},
      primaryClass={cs.GR},
      url={https://arxiv.org/abs/2310.08997}, 
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 12/9/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤

```
git clone --recursive https://github.com/osqp/osqp
cd osqp/
mkdir osqp-installed
mkdir build && cd build
cmake .. -DBUILD_SHARED_LIBS=ON
make -j
```