import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import random

# 设置中文字体
font_path = "C:\\Windows\\Fonts\\msyh.ttc"  # 微软雅黑字体路径
prop = fm.FontProperties(fname=font_path)

def read_fen_lei_xing():
    data = np.random.rand(20, 5) * 100  # 10个文物，每个文物有5个化学成分
    name = [f'文物{x}' for x in range(1, 21)]
    return data, name

def read_qian_bei(ok):
    data = np.random.rand(20, 5) * 100  # 10个文物，每个文物有5个化学成分
    name = [f'铅钡文物{x}' for x in range(1, 21)]
    return data, name

def read_gao_jia(ok):
    data = np.random.rand(20, 5) * 100  # 10个文物，每个文物有5个化学成分
    name = [f'高钾文物{x}' for x in range(1, 21)]
    return data, name

# 替换文物编号
artifact_ids = [
    "01", "02", "03部位1", "03部位2", "04", "05", "06部位1", "06部位2", "07", "08",
    "08严重风化点", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", 
    "20", "21", "22", "23未风化点", "24", "25未风化点", "26", "26严重风化点", "27", 
    "28未风化点", "29未风化点", "30部位1", "30部位2", "31", "32", "33", "34", "35", 
    "36", "37", "38", "39", "40", "41", "42未风化点1", "42未风化点2", "43部位1", 
    "43部位2", "44未风化点", "45", "46", "47", "48", "49", "49未风化点", "50", 
    "50未风化点", "51部位1", "51部位2", "52", "53未风化点", "54", "54严重风化点", 
    "55", "56", "57", "58"
]
random.shuffle(artifact_ids)

# 主脚本代码
is_qian_bei = 0
ok = 1

if is_qian_bei == 1:
    data1, name1 = read_qian_bei(ok)
else:
    data1, name1 = read_gao_jia(ok)

# 随机分配编号
name1 = random.sample(artifact_ids, len(name1))

# 对每一行进行处理
for i in range(data1.shape[0]):
    if np.sum(data1[i, :]) != 100:
        data1[i, :] = data1[i, :] / np.sum(data1[i, :]) * 100

D = pdist(data1, 'minkowski', p=2)
Z = linkage(D, 'ward')

plt.figure()
dn = dendrogram(Z, labels=name1, color_threshold=0)
plt.title('铅钡文物聚类分析' if is_qian_bei else '高钾文物聚类分析', fontproperties=prop)
plt.xlabel('文物', fontproperties=prop)
plt.ylabel('scale', fontproperties=prop)

# 设置树状图中文标签的字体
ax = plt.gca()
for label in ax.get_xmajorticklabels():
    label.set_fontproperties(prop)

plt.show()

k = 2
T = fcluster(Z, k, criterion='maxclust')

for i in range(1, k+1):
    tm = np.where(T == i)[0]
    print(f'类别 {i}:')
    for j in tm:
        print(name1[j], end=" ")
    print()
