import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取CSV数据
df = pd.read_csv('bb-week2.csv')

# 将 'parsedDate' 列转换为日期时间对象
df['parsedDate'] = pd.to_datetime(df['parsedDate'])

# 添加健康状态列
df['health_status'] = df['statusVal'].apply(lambda x: 'Healthy' if x == 1 else 'Unhealthy')

# 箱线图
plt.figure(figsize=(12, 8))
sns.boxplot(x='health_status', y='numProcs', data=df)
plt.title('Boxplot of numProcs by Health Status')
plt.show()

plt.figure(figsize=(12, 8))
sns.boxplot(x='health_status', y='loadAveragePercent', data=df)
plt.title('Boxplot of Load Average Percent by Health Status')
plt.show()

plt.figure(figsize=(12, 8))
sns.boxplot(x='health_status', y='physicalMemoryUsagePercent', data=df)
plt.title('Boxplot of Physical Memory Usage Percent by Health Status')
plt.show()

plt.figure(figsize=(12, 8))
sns.boxplot(x='health_status', y='connMade', data=df)
plt.title('Boxplot of Connection Made by Health Status')
plt.show()

# 相关性矩阵
correlation_matrix = df[['numProcs', 'loadAveragePercent', 'physicalMemoryUsagePercent', 'connMade']].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Selected Health Metrics')
plt.show()
