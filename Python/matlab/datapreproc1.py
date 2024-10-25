import pandas as pd

path = r"c:\Users\hemingyang\Documents\Tencent Files\2433986180\FileRecv\2022C题附件.xlsx"
df1 = pd.read_excel(path, '表单1')
column_data = df1.iloc[:, 3]  #第几列,注意索引从0开始为第一列
mode_value = column_data.mode()[0]  #获取并选择第一个众数
df1.iloc[:, 3] = column_data.fillna(mode_value) #使用众数填充
df2 = pd.read_excel(path, '表单2')
column_data = df2.iloc[:, :] 
df2.iloc[:, :] = column_data.fillna(0.04) #填充为最小比例0.04
df2.replace(0, 0.04, inplace=True)  #将0值替换为0.04
df3 = pd.read_excel(path, '表单3')
column_data = df3.iloc[:, :] 
df3.iloc[:, :] = column_data.fillna(0.04) #填充为最小比例0.04
df3.replace(0, 0.04, inplace=True) #将0值替换为0.04
with pd.ExcelWriter('proced3.xlsx', engine='openpyxl') as writer:
    df1.to_excel(writer, sheet_name='表单1', index=False)
    df2.to_excel(writer, sheet_name='表单2', index=False)
    df3.to_excel(writer, sheet_name='表单3', index=False)
