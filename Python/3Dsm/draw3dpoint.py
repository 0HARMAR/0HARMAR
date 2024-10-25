import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 创建一个新的图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 生成三维点
x = np.random.rand(10)
y = np.random.rand(10)
z = np.random.rand(10)

# 绘制三维点
ax.scatter(x, y, z)

# 设置坐标轴标签
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# 显示图形
plt.show()
