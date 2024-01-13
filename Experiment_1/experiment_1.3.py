import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 1. 读取Excel文件，将"?"替换为NaN
data = pd.read_excel('lab1_information.xlsx', sheet_name='adault', na_values=[" ?"])
# 2. 统计缺失值情况
missing_data = data.isnull().sum()
print("缺失值情况：")
print(missing_data)
# 3. 可视化缺失值分布
plt.figure(figsize=(10, 6))
sns.heatmap(data.isnull(), cbar=False, cmap='viridis')
plt.title('Missing value distribution')
plt.show()
# 填充数字缺失值
numeric_columns = data.select_dtypes(include=['int64', 'float64']).columns
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())
# 填充文字缺失值
text_columns = data.select_dtypes(include=['object']).columns
for column in text_columns:
    data[column] = data[column].fillna(method='ffill')
# 6. 保存填充后的数据
data.to_excel('lab1_information_filled.xlsx', index=False)
