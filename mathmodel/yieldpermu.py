import pandas as pd
import matplotlib.pyplot as plt

# 读取数据表
df = pd.read_excel('mathmodel/C题/附件2.xlsx', sheet_name=1)

# 确保 '作物编号' 列是数值类型（如果可能）
df['作物编号'] = pd.to_numeric(df['作物编号'], errors='coerce')

# 删除包含 NaN 的行
df = df.dropna(subset=['作物编号', '亩产量/斤'])

# 提取数据
x = df['作物编号']
y = df['亩产量/斤']

# 绘制柱状图
plt.figure(figsize=(10, 6))
plt.bar(x, y, color='skyblue', edgecolor='black')
plt.xlabel('crop number')
plt.ylabel('yield per mu')
plt.title('yield per mu')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.savefig('/mnt/Just-For-Fun/mathmodel/yieldpermu.png')
