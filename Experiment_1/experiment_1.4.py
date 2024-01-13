import pandas as pd
# 读取数据集
data = pd.read_csv("network_lab1.csv")
# 统计数据的基本情况
data_info = data.describe()
# 判断是否有缺失值的属性
missing_values = data.isnull().sum()
# 输出统计情况为Excel文件
data_info.to_excel("data_info.xlsx", sheet_name="Data Info")
missing_values.to_excel("missing_values.xlsx", sheet_name="Missing Values")
# 删除包含缺失值的记录
data_cleaned = data.dropna()
# 另存为csv文件
data_cleaned.to_csv("data_cleaned.csv", index=False)
