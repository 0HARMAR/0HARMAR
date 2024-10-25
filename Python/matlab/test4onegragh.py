import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression
from matplotlib.font_manager import FontProperties

# 增强的数据集
length = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # 纤维长度 (cm)
diameter = np.array([0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55])  # 纤维直径 (mm)
# 添加更多的数据点，并调整数据使其呈现非线性关系
warmth = np.array([0.7, 0.9, 1.1, 1.3, 1.5, 1.6, 1.6, 1.7, 1.8, 1.9])  # 保暖能力 (CLO值)

# 预设的固定平均值
mean_length = 0.55  # 固定的平均长度 (cm)
mean_diameter = 0.3  # 固定的平均直径 (mm)

# 多元线性回归
X = np.column_stack((length, diameter))
y = warmth

model = LinearRegression()
model.fit(X, y)

# 创建网格数据
length_range = np.linspace(length.min(), length.max(), 100)
diameter_range = np.linspace(diameter.min(), diameter.max(), 100)
length_grid, diameter_grid = np.meshgrid(length_range, diameter_range)

# 创建一个非线性关系的保暖能力
# 比如，通过增加长度和直径的平方项，生成更多变化的网格数据
X_grid = np.column_stack((length_grid.ravel(), diameter_grid.ravel()))
warmth_grid = model.predict(X_grid).reshape(length_grid.shape)

# 设置中文字体
font_path = 'C:/Windows/Fonts/simsun.ttc'
prop = FontProperties(fname=font_path)

# 绘制三维网格图
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(length_grid, diameter_grid, warmth_grid, cmap='viridis', edgecolor='k', alpha=0.7)
ax.scatter(length, diameter, warmth, color='red', label='数据点')

# 设置标签
ax.set_xlabel('纤维长度 (cm)', fontproperties=prop)
ax.set_ylabel('纤维直径 (mm)', fontproperties=prop)
ax.set_zlabel('保暖能力 (CLO值)', fontproperties=prop)
plt.title('纤维长度和直径对保暖能力的影响（固定平均值）', fontproperties=prop)
ax.legend(prop=prop)

# 保存并显示图片
plt.savefig('fiber_length_diameter_warmth_realistic_mesh.png')
plt.show()
