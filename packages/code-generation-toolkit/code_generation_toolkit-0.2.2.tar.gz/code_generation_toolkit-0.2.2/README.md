# CG-Kit: Code Generation tool-Kit for algorithmic and performance portability

The development of CG-Kit addresses the shifting landscape of high-performance
computing (HPC) platforms and the algorithmic complexities of large-scale
scientific applications.  The key challenges that CG-Kit aims to solve include
handling a large code base in Fortran and/or C/C++, subdivision of code into
large numbers of units supporting a wide range of physics and numerical
methods, different parallelization techniques for distributed and shared memory
systems and accelerator devices, and heterogeneity of computing platforms
requiring coexisting variants of parallel algorithms.  CG-Kit tackles the
challenges by providing users with the ability to express their desired control
flow and computation-to-resource map in the form a pseudocode-like recipe.  It
consists of standalone tools that can be combined into highly specific and
effective portability and maintainability toolchains.

Algorithmic variants are different realizations of numerical algorithms that
lead to the same solution outcome but differ in the details of algorithm design
and/or the implementation of how the solution is obtained.  The need for
variants arises from differences in hardware architecture, and maintaining all
variants explicitly is challenging. CG-Kit introduces a feasible way of
handling variants and thereby achieves **algorithmic portability**, where
algorithms are adapted to hardware platforms.

## Tools

- `cflow`: Control Flow Graphs
- `ctree`: Source Code Trees

## Install

Install the latest version of CG-Kit:
```bash
python -m pip install code-generation-toolkit
```

## License

Released under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

## Citation

Paper on [arxiv](https://arxiv.org/abs/2401.03378):
```tex
@Article{RudiLeeChadhaEtAl24,
  title={{CG}-{K}it: Code Generation Toolkit for Performant and Maintainable
         Variants of Source Code Applied to {F}lash-{X} Hydrodynamics
         Simulations},
  author={Rudi, Johann and Lee, Youngjun and Chadha, Aidan H and Wahib, Mohamed
          and Weide, Klaus and O'Neal, Jared P and Dubey, Anshu},
  year={2024},
  note={arXiv preprint arXiv:2401.03378}
}
```
