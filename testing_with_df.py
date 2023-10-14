from read_txt_data import read_txt
import matplotlib.pyplot as plt
import numpy as np

df = read_txt("uniform-250-10-3d.txt")

df = df[df["level"] == 1]

df["x"] = df["x"]*10
df["y"] = df["y"]*10
df["z"] = df["z"]*10

# 2nd input points

x_data = df["x"].tolist()
y_data = df["y"].tolist()
z_data = df["z"].tolist()

x_max = np.max(np.array(x_data, dtype = int)) + 2
y_max = np.max(np.array(y_data, dtype = int)) + 2
z_max = np.max(np.array(z_data, dtype = int)) + 2

x, y, z = np.indices((x_max, y_max, z_max))

cubes_list = []
n_cubes = len(x_data)

for i in range(0, n_cubes):
	_x = x_data[i]
	_y = y_data[i]
	_z = z_data[i]

	cubes_list.append((x < _x) & (y < _y) & (z < _z))

voxelarray = np.zeros((x_max, y_max, z_max), dtype = bool)

for i in range(0, n_cubes):
	voxelarray = voxelarray | cubes_list[i]

ax = plt.figure().add_subplot(projection='3d')
ax.voxels(voxelarray, facecolors = "cyan", edgecolor = None, linewidth = 0.5)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.show()