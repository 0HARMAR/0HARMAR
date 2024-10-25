import pandas as pd
import numpy as np

# 加载数据
file_path = r"c:\Users\hemingyang\Documents\Tencent Files\2433986180\FileRecv\2022C题附件.xlsx"
sheet2_data = pd.read_excel(file_path, sheet_name='表单2')

# 剔除含有空值和零值的行
valid_data = sheet2_data.dropna().replace(0, np.nan).dropna()

# 选择数值列
numeric_cols = valid_data.select_dtypes(include='number').columns

# 计算每一行的总和
row_sums = valid_data[numeric_cols].sum(axis=1)

# 将每一行的每个成分除以该行的总和
normalized_data = valid_data[numeric_cols].div(row_sums, axis=0)

# 计算每一行的几何平均数
geometric_means = normalized_data.apply(lambda row: np.exp(np.mean(np.log(row))), axis=1)

# 计算中心化对数比变换
clr_data = normalized_data.apply(lambda row: np.log(row / geometric_means[row.name]), axis=1)

# 合并处理后的数据和原始非数值列
final_data = pd.concat([valid_data.drop(columns=numeric_cols), clr_data], axis=1)

# 将处理后的表单2写回原Excel文件
with pd.ExcelWriter(file_path, mode='a', if_sheet_exists='replace') as writer:
    final_data.to_excel(writer, sheet_name='表单2', index=False)

print("Processed data has been saved back to the original Excel file.")
