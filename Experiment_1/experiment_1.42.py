import pandas as pd
import matplotlib.pyplot as plt
# 读取数据集
data = pd.read_csv("network_lab1.csv")
data = data[data[" Label"] != "BENIGN"]
# 统计不同攻击类型的数量
attack_counts = data[" Label"].value_counts()
# 使用图表展示攻击类型及数量
plt.figure(figsize=(12, 6))
attack_counts.plot(kind="bar")
plt.title("Distribution of Attack Types")
plt.xlabel("Attack Type")
plt.ylabel("Count")
plt.xticks(rotation=90)  # 旋转 x 轴标签以便显示更多类型
plt.show()
