import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
file_path = 'mathmodel/C题/附件1.xlsx'  # 请替换为实际文件路径
df = pd.read_excel(file_path)

# 假设我们要根据'地块类型'来展示每种类型的面积占比
# 首先，我们需要对数据按'地块类型'进行分组并计算总面积
area_summary = df.groupby('地块类型')['地块面积/亩'].sum()

# 绘制饼图
plt.figure(figsize=(10, 8))
plt.pie(area_summary, labels=area_summary.index, autopct='%1.1f%%', startangle=140)
plt.title('Area Proportion by Land Type')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# 显示图表
plt.savefig("mathmodel/bingtu.png")