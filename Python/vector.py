import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义向量
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

# 计算向量积，得到法向量
normal_vector = np.cross(vector1, vector2)

# 创建一个网格
xx, yy = np.meshgrid(range(-10, 10), range(-10, 10))

# 计算网格点的z坐标，使得这些点满足平面方程 ax + by + cz = 0
# 平面方程为 normal_vector[0]*x + normal_vector[1]*y + normal_vector[2]*z = 0
# 即 z = -(normal_vector[0]*x + normal_vector[1]*y) / normal_vector[2]
z = -(normal_vector[0] * xx + normal_vector[1] * yy) / normal_vector[2]

# 创建3D图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制平面
ax.plot_surface(xx, yy, z, alpha=0.5, rstride=100, cstride=100)

# 绘制向量
ax.quiver(0, 0, 0, vector1[0], vector1[1], vector1[2], color='r', label='Vector 1')
ax.quiver(0, 0, 0, vector2[0], vector2[1], vector2[2], color='b', label='Vector 2')

# 设置坐标轴
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.legend()
plt.show()
