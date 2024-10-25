import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 数据
materials = ['棉花', '羽绒', '聚酯纤维', '聚丙烯纤维', '聚酰胺纤维', '再生纤维']
labels = ['热导率', '热阻值', '总热导传系数', 'CLO值', '纤维厚度', '纤维密度']
data = np.array([
    [0.037, 0.027, 0.04, 0.2, 0.25, 0.25],         # 热导率
    [0.037, 2, 0.9, 0.32, 0.32, 0.32],             # 热阻值
    [0.04, 0.035, 0.03, 0.32, 0.32, 0.32],         # 总热导传系数
    [0.5, 1.125, 0.8, 0.9, 0.7, 0.6],              # CLO值
    [0.015, 0.2, 0.18, 0.16, 0.04, 0.04],          # 纤维厚度 (cm)
    [1.5, 0.7, 1.38, 0.91, 1.15, 1.5]              # 纤维密度
])

# 创建热图
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(data, annot=True, fmt=".2f", xticklabels=materials, yticklabels=labels, cmap="YlGnBu")

# 添加标签
font_path = 'C:/Windows/Fonts/simsun.ttc'
prop = FontProperties(fname=font_path)
plt.xlabel('材料', fontproperties=prop)
plt.ylabel('指标', fontproperties=prop)
plt.title('不同材料的指标热图', fontproperties=prop)

# 更新标签字体
ax.set_xticklabels(ax.get_xticklabels(), fontproperties=prop)
ax.set_yticklabels(ax.get_yticklabels(), fontproperties=prop)

# 保存并显示图片
plt.savefig('fiber_comparison_heatmap.png')
plt.show()
