import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 从 CSV 文件读取数据
df = pd.read_csv('mathmodel/C题/')

# 检查数据的列名和数据类型
print(df.head())
print(df.columns)

# 选择需要的列
# 假设 CSV 文件中有 '地块类型', '种植季次', 和 '亩产量' 列
# 你需要根据实际情况调整列名
crop_names = df['作物名称']
field_types = df['地块类型']
seasons = df['种植季次']
yield_values = df['亩产量']

# 将类别变量转换为数字
field_types_numeric = pd.factorize(field_types)[0]
seasons_numeric = pd.factorize(seasons)[0]

# 绘制三维网格图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 将数据绘制为三维散点图
scatter = ax.scatter(field_types_numeric, seasons_numeric, yield_values, c=yield_values, cmap='viridis')

# 设置轴标签
ax.set_xlabel('Field Type')
ax.set_ylabel('Season')
ax.set_zlabel('Yield')
ax.set_xticks(np.unique(field_types_numeric))
ax.set_xticklabels(np.unique(field_types))
ax.set_yticks(np.unique(seasons_numeric))
ax.set_yticklabels(np.unique(seasons))

# 添加颜色条
fig.colorbar(scatter, ax=ax, label='Yield')

# 显示图形
plt.show()
