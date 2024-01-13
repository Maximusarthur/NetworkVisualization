import pandas as pd

# 读取CSV数据
df = pd.read_csv('nf-week2.csv')

# 打印处理前的情况
print("处理前:")
print("缺失值情况:\n", df.isnull().sum())
print("重复值数量:", df.duplicated().sum())

# 处理缺失值并删除重复行
df = df.dropna()
df = df.drop_duplicates()

# 打印处理后的情况
print("\n处理后:")
print("缺失值情况:\n", df.isnull().sum())
print("重复值数量:", df.duplicated().sum())

# 保存处理后的数据到新的CSV文件
df.to_csv('processed_data.csv', index=False)
