import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 材料和数据
materials = ['棉花', '羽绒', '聚酯纤维', '聚丙烯纤维', '聚酰胺纤维', '再生纤维']
data = np.array([
    [0.045, 0.117, 0.04, 0.2, 0.3, 0.045],         # 热导率
    [0.65, 0.25, 0.15, 0.25, 0.026, 0.55],             # 热阻值
    [0.04, 0.025, 0.03, 0.2, 0.2, 0.04],         # 总热导传系数
    [0.4, 1.125, 0.5, 0.4, 0.5, 0.6],              # CLO值
    [0.15,  2, 1.8, 1.6, 0.4,0.4],          # 纤维厚度 (cm)
    [0.25, 0.1, 1.38, 0.9, 1.15, 1.5]              # 纤维密度
])

# 定义权重
weights = np.array([0.2, 0.3, 0.2, 0.1, 0.1, 0.1])

# 归一化数据
data_norm = np.zeros_like(data)
for i in range(data.shape[0]):
    min_val = np.min(data[i, :])
    max_val = np.max(data[i, :])
    if min_val == max_val:
        data_norm[i, :] = 0
    else:
        data_norm[i, :] = (data[i, :] - min_val) / (max_val - min_val)

# 计算综合评分
scores = np.dot(weights, data_norm)

# 创建雷达图
labels = ['热导率', '热阻值', '总热导传系数', 'CLO值', '纤维厚度', '纤维密度']
num_vars = len(labels)

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# 绘制每种纤维的雷达图
for i, material in enumerate(materials):
    values = data_norm[:, i].tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=material)
    ax.fill(angles, values, alpha=0.25)

# 添加标签
font_path = 'C:/Windows/Fonts/simsun.ttc'
prop = FontProperties(fname=font_path)
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

ax.set_rlabel_position(0)
plt.xticks(angles[:-1], labels, fontproperties=prop)
plt.yticks([0.2, 0.4, 0.6, 0.8, 1.0], ["0.2", "0.4", "0.6", "0.8", "1.0"], color="grey", size=7)
plt.ylim(0, 1)

# 添加图例
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), prop=prop)

# 保存并显示图片
plt.savefig('fiber_comparison_radar.png')
plt.show()
