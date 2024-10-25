import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from matplotlib.font_manager import FontProperties

# 数据
length = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # 纤维长度 (cm)
diameter = np.array([0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55])  # 纤维直径 (mm)
warmth = np.array([0.8, 1.0, 1.2, 1.3, 1.4, 1.5, 1.5, 1.6, 1.6, 1.7])  # 保暖能力 (CLO值)

# 多元线性回归
X = np.column_stack((length, diameter))
y = warmth

model = LinearRegression()
model.fit(X, y)

# 回归系数和截距
coef_length, coef_diameter = model.coef_
intercept = model.intercept_

# 打印结果
print(f'线性回归结果: 纤维长度系数 = {coef_length}, 纤维直径系数 = {coef_diameter}, 截距 = {intercept}')

# 可视化纤维长度和保暖能力的关系
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(length, warmth, label='数据点', color='blue')
plt.plot(length, model.predict(X) - coef_diameter * diameter, color='red', label='拟合线')
plt.xlabel('纤维长度 (cm)', fontproperties=FontProperties(fname='C:/Windows/Fonts/simsun.ttc'))
plt.ylabel('保暖能力 (CLO值)', fontproperties=FontProperties(fname='C:/Windows/Fonts/simsun.ttc'))
plt.title('纤维长度对保暖能力的影响', fontproperties=FontProperties(fname='C:/Windows/Fonts/simsun.ttc'))
plt.legend(prop=FontProperties(fname='C:/Windows/Fonts/simsun.ttc'))

# 可视化纤维直径和保暖能力的关系
plt.subplot(1, 2, 2)
plt.scatter(diameter, warmth, label='数据点', color='blue')
plt.plot(diameter, model.predict(X) - coef_length * length, color='red', label='拟合线')
plt.xlabel('纤维直径 (mm)', fontproperties=FontProperties(fname='C:/Windows/Fonts/simsun.ttc'))
plt.ylabel('保暖能力 (CLO值)', fontproperties=FontProperties(fname='C:/Windows/Fonts/simsun.ttc'))
plt.title('纤维直径对保暖能力的影响', fontproperties=FontProperties(fname='C:/Windows/Fonts/simsun.ttc'))
plt.legend(prop=FontProperties(fname='C:/Windows/Fonts/simsun.ttc'))

plt.tight_layout()
plt.savefig('fiber_length_diameter_warmth_relation.png')
plt.show()
