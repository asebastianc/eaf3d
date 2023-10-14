from read_txt_data import read_txt
import matplotlib.pyplot as plt
import numpy as np

# -------- Spherical

df_spherical = read_txt("spherical-250-10-3d.txt")

df_spherical = df_spherical[df_spherical["level"] == 1]

df_spherical["x"] = df_spherical["x"]*100
df_spherical["y"] = df_spherical["y"]*100
df_spherical["z"] = df_spherical["z"]*100

# 2nd input points

x_data_spherical = df_spherical["x"].tolist()
y_data_spherical = df_spherical["y"].tolist()
z_data_spherical = df_spherical["z"].tolist()

x_max_spherical = np.max(np.array(x_data_spherical, dtype = int)) + 2
y_max_spherical = np.max(np.array(y_data_spherical, dtype = int)) + 2
z_max_spherical = np.max(np.array(z_data_spherical, dtype = int)) + 2

x_spherical, y_spherical, z_spherical = np.indices((x_max_spherical, y_max_spherical, z_max_spherical))

cubes_list_spherical = []
n_cubes_spherical = len(x_data_spherical)

for i in range(0, n_cubes_spherical):
	_x = x_data_spherical[i]
	_y = y_data_spherical[i]
	_z = z_data_spherical[i]

	cubes_list_spherical.append((x_spherical < _x) & (y_spherical < _y) & (z_spherical < _z))

voxelarray_spherical = np.zeros((x_max_spherical, y_max_spherical, z_max_spherical), dtype = bool)

for i in range(0, n_cubes_spherical):
	voxelarray_spherical = voxelarray_spherical | cubes_list_spherical[i]


# -------- Uniform

df_uniform = read_txt("uniform-250-10-3d.txt")

df_uniform = df_uniform[df_uniform["level"] == 1]

df_uniform["x"] = df_uniform["x"]*10
df_uniform["y"] = df_uniform["y"]*10
df_uniform["z"] = df_uniform["z"]*10

# 2nd input points

x_data_uniform = df_uniform["x"].tolist()
y_data_uniform = df_uniform["y"].tolist()
z_data_uniform = df_uniform["z"].tolist()

x_max_uniform = np.max(np.array(x_data_uniform, dtype = int)) + 2
y_max_uniform = np.max(np.array(y_data_uniform, dtype = int)) + 2
z_max_uniform = np.max(np.array(z_data_uniform, dtype = int)) + 2

x_uniform, y_uniform, z_uniform = np.indices((x_max_uniform, y_max_uniform, z_max_uniform))

cubes_list_uniform = []
n_cubes_uniform = len(x_data_uniform)

for i in range(0, n_cubes_uniform):
	_x = x_data_uniform[i]
	_y = y_data_uniform[i]
	_z = z_data_uniform[i]

	cubes_list_uniform.append((x_uniform < _x) & (y_uniform < _y) & (z_uniform < _z))

voxelarray_uniform = np.zeros((x_max_uniform, y_max_uniform, z_max_uniform), dtype = bool)

for i in range(0, n_cubes_uniform):
	voxelarray_uniform = voxelarray_uniform | cubes_list_uniform[i]



ax = plt.figure().add_subplot(projection='3d')
ax.voxels(voxelarray_uniform, facecolors = "blue", edgecolor = None, linewidth = 0.5, alpha = 0.7)
ax.voxels(voxelarray_spherical, facecolors = "red", edgecolor = None, linewidth = 0.5, alpha = 0.7)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()