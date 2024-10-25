import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

# 指定字体路径
font_path = 'C:/Windows/Fonts/simhei.ttf'  # Windows路径
# font_path = '/usr/share/fonts/truetype/simhei.ttf'  # Linux路径

# 创建字体对象
my_font = font_manager.FontProperties(fname=font_path)

# 生成一些数据
np.random.seed(10)
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# 创建箱线图
plt.boxplot(data, vert=True, patch_artist=True)
plt.title("箱线图示例", fontproperties=my_font)
plt.xlabel("类别", fontproperties=my_font)
plt.ylabel("值", fontproperties=my_font)
plt.show()
