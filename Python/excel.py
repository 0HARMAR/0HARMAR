import pandas as pd

# 创建示例数据
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# 创建DataFrame
df = pd.DataFrame(data)

# 将DataFrame写入Excel文件
df.to_excel('output.xlsx', index=False)
