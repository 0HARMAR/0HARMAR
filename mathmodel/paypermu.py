import pandas as pd
import matplotlib.pyplot as plt

# 读取数据表
df = pd.read_excel('mathmodel/C题/附件2.xlsx', sheet_name=1)

# 确保 '作物编号' 列是数值类型（如果可能）
df['作物编号'] = pd.to_numeric(df['作物编号'], errors='coerce')

# 删除包含 NaN 的行
df = df.dropna(subset=['作物编号', '种植成本/(元/亩)'])

# 提取数据
x = df['作物编号']
cost = df['种植成本/(元/亩)']

# 绘制散点图
plt.figure(figsize=(10, 6))
plt.scatter(x, cost, color='skyblue', edgecolor='black', s=100)  # s 是点的大小
plt.xlabel('Crop Number')
plt.ylabel('Cost per Mu')
plt.title('Cost per Mu')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# 保存图形
plt.savefig('/mnt/Just-For-Fun/mathmodel/cost_per_mu.png')

# 显示图形
plt.show()
