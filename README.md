# EAF 3D Visualization

This **repository** includes a first draft of an 3D Visualization of Empirical Attainment Function (EAF) results.

Specifically, this repository plots the following two results from the [EAF package](https://github.com/MLopez-Ibanez/eaf):
1. `uniform-250-10-3d.txt`.
2. `spherical-250-10-3d.txt`.

### Requisites
- `Python` is required for reproducing the analysis. Further documentation [here](https://www.python.org/).
  - The `pandas` package is required for data manipulation and to get real time data.
  - The `numpy` package is required for mathematical formulations.
  - The `matplotlib` package is required for plots.

## EAF results data

This project utilizes the both: `uniform-250-10-3d.txt` and `spherical-250-10-3d.txt` files.

Theese files, used as input, have been sourced from [here](https://github.com/MLopez-Ibanez/eaf/blob/master/inst/extdata).

## Plots & Reproducibility

In order to obtain the EAF 3D plots, it is only necessary to run either:

- `testing_with_df.py`: to plot the first level of the `uniform-250-10-3d.txt` dataset.
- `test_uniform_vs_spherical.py`: to plot the first level of the `uniform-250-10-3d.txt` and `spherical-250-10-3d.txt` datasets in the same canvas.
