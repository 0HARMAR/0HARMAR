import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster, cophenet
import matplotlib.pyplot as plt

# 定义一些自定义函数
def read_qian_bei(ok):
    # 这里需要实现读取千贝数据的函数
    pass

def read_gao_jia(ok):
    # 这里需要实现读取高甲数据的函数
    pass

def read_pred():
    # 这里需要实现读取预测数据的函数
    pass

def getY(p, x):
    # 计算多项式的值
    return np.polyval(p, x)

# 主程序
is_qian_bei = 0
ok = 1

if is_qian_bei == 1:
    data1, name1 = read_qian_bei(ok)
else:
    data1, name1 = read_gao_jia(ok)

D = pdist(data1, 'minkowski', 2)
Z = linkage(D, 'ward')
H = dendrogram(Z, labels=name1)
plt.setp(H, color='k', linewidth=1.3)

if is_qian_bei == 1:
    plt.title('千贝分类', fontsize=16)
else:
    plt.title('高甲分类', fontsize=16)

plt.xlabel('City', fontsize=12)
plt.ylabel('Scale', fontsize=12)
plt.show()

k = 2
T = fcluster(Z, k, criterion='maxclust')

for i in range(1, k + 1):
    tm = np.where(T == i)[0]
    print(f'Cluster {i}:', ', '.join(name1[j] for j in tm))

# 对第一个簇进行重新聚类
z1 = np.where(T == 1)[0]
D = pdist(data1[z1, :], 'minkowski', 2)
Z = linkage(D, 'ward')
name11 = [name1[j] for j in z1]
H = dendrogram(Z, labels=name11)
plt.xlabel('City')
plt.ylabel('Scale')
plt.show()

T1 = fcluster(Z, k, criterion='maxclust')

for i in range(1, k + 1):
    tm = np.where(T1 == i)[0]
    print(f'Cluster {i}:', ', '.join(name11[j] for j in tm))

# 对第二个簇进行重新聚类
z2 = np.where(T == 2)[0]
D = pdist(data1[z2, :], 'minkowski', 2)
Z = linkage(D, 'ward')
name12 = [name1[j] for j in z2]
H = dendrogram(Z, labels=name12)
plt.xlabel('City')
plt.ylabel('Scale')
plt.show()

T2 = fcluster(Z, k, criterion='maxclust')
T2 += 2

for i in range(3, k + 3):
    tm = np.where(T2 == i)[0]
    print(f'Cluster {i}:', ', '.join(name12[j] for j in tm))

z12 = np.concatenate([z1, z2])
T12 = np.concatenate([T1, T2])
ind = np.argsort(z12)
T12 = T12[ind]

# 计算每个簇的均值
fea = np.ones((14, 4))
for i in range(14):
    for t in range(4):
        fea[i, t] = np.mean(data1[T12 == t, i])

fea = fea.T
fea = fea[[0, 1, 3, 2], :]

x0 = np.arange(1, 5)
x1 = np.arange(1, 4.2, 0.2)

fea_name = [
    "SiO2", "Na2O", "K2O", "CaO", "MgO", "Al2O3", "Fe2O3", "CuO", 
    "PbO", "BaO", "P2O5", "SrO", "SnO2", "SO2"
]

a, b = 1, 14
p = np.zeros((14, 3))

for i in range(a, b + 1):
    p[i - 1, :] = np.polyfit(x0, fea[:, i - 1], 2)
    y1 = np.polyval(p[i - 1, :], x1)
    plt.figure()
    plt.plot(x0, fea[:, i - 1], '*', linewidth=5)
    plt.plot(x1, y1, 'o')
    plt.legend(['Original', 'Fitted'])
    plt.xlabel('Cluster')
    plt.title(fea_name[i - 1])
    plt.show()

qian_bei3, qian_bei4, gao_jia3, gao_jia4 = read_pred()
qian_bei_pred4 = np.zeros_like(qian_bei4)
gao_jia_pred4 = np.zeros_like(gao_jia4)
qian_bei_pred3 = np.zeros_like(qian_bei3)
gao_jia_pred3 = np.zeros_like(gao_jia3)

if is_qian_bei == 1:
    for i in range(qian_bei4.shape[0]):
        for j in range(a, b + 1):
            if j == 5 or j == 3:
                qian_bei_pred4[i, j] = qian_bei4[i, j]
                continue
            if qian_bei4[i, j] > 0:
                qian_bei_pred4[i, j] = np.sqrt(qian_bei4[i, j] - getY(p[j - 1, :], 4)) + getY(p[j - 1, :], 1)
            else:
                qian_bei_pred4[i, j] = -np.sqrt(-qian_bei4[i, j] - getY(p[j - 1, :], 4)) + getY(p[j - 1, :], 1)
    
    for i in range(qian_bei3.shape[0]):
        for j in range(a, b + 1):
            if j == 5 or j == 3:
                qian_bei_pred3[i, j] = qian_bei3[i, j]
                continue
            if qian_bei3[i, j] > 0:
                qian_bei_pred3[i, j] = np.sqrt(qian_bei3[i, j] - getY(p[j - 1, :], 4)) + getY(p[j - 1, :], 1)
            else:
                qian_bei_pred3[i, j] = -np.sqrt(-qian_bei3[i, j] - getY(p[j - 1, :], 4)) + getY(p[j - 1, :], 1)
    
    np.savetxt('../qian_bei4.csv', qian_bei_pred4, delimiter=',')
    np.savetxt('../qian_bei3.csv', qian_bei_pred3, delimiter=',')
else:
    for i in range(gao_jia4.shape[0]):
        for j in range(a, b + 1):
            if j == 14 or j == 13 or j == 2:
                gao_jia_pred4[i, j] = gao_jia4[i, j]
                continue
            if gao_jia4[i, j] > 0:
                gao_jia_pred4[i, j] = np.sqrt(gao_jia4[i, j] - getY(p[j - 1, :], 4)) + getY(p[j - 1, :], 1)
            else:
                gao_jia_pred4[i, j] = -np.sqrt(-gao_jia4[i, j] - getY(p[j - 1, :], 4)) + getY(p[j - 1, :], 1)
    
    for i in range(gao_jia3.shape[0]):
        for j in range(a, b + 1):
            if j == 14 or j == 13 or j == 2:
                gao_jia_pred3[i, j] = gao_jia3[i, j]
                continue
            if gao_jia3[i, j] > 0:
                gao_jia_pred3[i, j] = np.sqrt(gao_jia3[i, j] - getY(p[j - 1, :], 4)) + getY(p[j - 1, :], 1)
            else:
                gao_jia_pred3[i, j] = -np.sqrt(-gao_jia3[i, j] - getY(p[j - 1, :], 4)) + getY(p[j - 1, :], 1)
    
    np.savetxt('../gao_jia_pred4.csv', gao_jia_pred4, delimiter=',')
    np.savetxt('../gao_jia_pred3.csv', gao_jia_pred3, delimiter=',')
