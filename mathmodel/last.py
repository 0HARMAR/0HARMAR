import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 提取 DataFrame 的数据
land_indices = result_df.index
crop_names = result_df.columns
X, Y = np.meshgrid(land_indices, range(len(crop_names)))
Z = np.array(result_df)

# 绘制 3D 柱状图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制每个柱状图
for i in range(len(crop_names)):
    ax.bar(X[:, i], Z[:, i], zs=i, zdir='y', alpha=0.8)

# 设置标签
ax.set_xlabel('地块编号')
ax.set_ylabel('作物类型')
ax.set_zlabel('占比')
ax.set_yticks(range(len(crop_names)))
ax.set_yticklabels(crop_names)

plt.show()
