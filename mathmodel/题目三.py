import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# 设置随机种子
np.random.seed(0)

# 作物和年份的数量
num_crops = 41
num_years = 54

# 模拟作物产量、价格、作物类型和种植成本
crop_yield = np.random.normal(loc=1000, scale=200, size=(num_crops, num_years))
crop_price = np.random.normal(loc=5.0, scale=1.0, size=(num_crops, num_years))

# 6种作物类型
crop_type = np.random.choice(['AL', 'Tr', 'Hl', 'IL', 'RG', 'SG'], size=num_crops)
# 种植成本在100到1000之间
planting_cost = np.random.uniform(100, 1000, size=(num_crops, num_years))

# 将所有数据整合为 DataFrame
data = pd.DataFrame({
    'Crop_Yield': crop_yield.flatten(),
    'Crop_Price': crop_price.flatten(),
    'Planting_Cost': planting_cost.flatten(),
    'Crop_Type': np.repeat(crop_type, num_years)
})

# 进行 Kolmogorov-Smirnov 检验
ks_results = {}
for column in ['Crop_Yield', 'Crop_Price', 'Planting_Cost']:
    ks_stat, ks_p_value = stats.kstest(data[column], 'norm', args=(data[column].mean(), data[column].std()))
    ks_results[column] = (ks_stat, ks_p_value)

print("Kolmogorov-Smirnov Test Results:")
for feature, result in ks_results.items():
    print(f"{feature}: Statistic={result[0]:.4f}, P-value={result[1]:.4f}")

# 进行 Shapiro-Wilk 检验
shapiro_results = {}
for column in ['Crop_Yield', 'Crop_Price', 'Planting_Cost']:
    shapiro_stat, shapiro_p_value = stats.shapiro(data[column])
    shapiro_results[column] = (shapiro_stat, shapiro_p_value)

print("\nShapiro-Wilk Test Results:")
for feature, result in shapiro_results.items():
    print(f"{feature}: Statistic={result[0]:.4f}, P-value={result[1]:.4f}")

# 绘制数据的直方图、正态分布曲线和作物类型分布的柱状图
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
features = ['Crop_Yield', 'Crop_Price', 'Planting_Cost']

for i, feature in enumerate(features):
    ax = axes[i // 2, i % 2]
    ax.hist(data[feature], bins=20, alpha=0.7, color='blue', density=True)
    
    # 绘制正态分布曲线
    mu, std = data[feature].mean(), data[feature].std()
    xmin, xmax = ax.get_xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, std)
    ax.plot(x, p, 'k', linewidth=2)
    ax.set_title(f'{feature} Distribution')

# 绘制作物类型的分布
ax = axes[1, 1]
crop_type_counts = data['Crop_Type'].value_counts()
ax.bar(crop_type_counts.index, crop_type_counts.values, color='green', alpha=0.7)
ax.set_title('Crop Type Distribution')
ax.set_ylabel('Frequency')

plt.tight_layout()
plt.savefig('/mnt/Just-For-Fun/mathmodel/distribution_plot.png')

# 根据检验结果提供建议
for feature in ks_results:
    ks_stat, ks_p_value = ks_results[feature]
    shapiro_stat, shapiro_p_value = shapiro_results[feature]
    if ks_p_value < 0.05 or shapiro_p_value < 0.05:
        print(f"{feature} data does not follow a normal distribution.")
    else:
        print(f"{feature} data follows a normal distribution.")
