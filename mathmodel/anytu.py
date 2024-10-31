import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
file_path = 'mathmodel/C题/附件2.xlsx'  # 请替换为实际文件路径
df = pd.read_excel(file_path)

# 选择展示作物名称和作物类型的数据
plt.figure(figsize=(12, 8))

# 为每种作物类型创建一个条形图
num_categories = len(df['作物类型'].unique())
bar_width = 0.35
index = pd.Index(df['作物名称'])  # 作物名称作为x轴标签

# 为每种作物类型设置一个位置
for i, crop_type in enumerate(df['作物类型'].unique()):
    subset = df[df['作物类型'] == crop_type]
    plt.bar(index + bar_width * i, subset['种植面积/亩'], bar_width, label=crop_type)

plt.title('Planting Area by Crop Name and Type')
plt.xlabel('Crop Name')
plt.ylabel('Planting Area (mu)')
plt.xticks(index, index, rotation=45)
plt.legend(title='Crop Type')

# 显示图形
plt.tight_layout()
plt.show()