import pandas as pd

# 读取数据集
data = pd.read_csv("network_lab1.csv")

# 分离正常数据
normal_data = data[data[" Label"] == "BENIGN"]
attack_types = data[" Label"].unique()  # 获取所有攻击类型

# 存储关键特征属性
key_features = {}

# 遍历攻击类型
for attack_type in attack_types:
    if attack_type == "BENIGN":
        continue  # 跳过正常流量
    attack_data = data[data[" Label"] == attack_type]

    # 选择数值列
    numeric_columns = data.select_dtypes(include=['number'])

    # 计算均值
    diff = attack_data[numeric_columns.columns].mean() - normal_data[numeric_columns.columns].mean()

    # 确定关键特征
    key_features[attack_type] = diff.abs().nlargest(5)  # 前5个关键特征

# 输出结果
for attack_type, features in key_features.items():
    print(f"关键特征属性 - {attack_type} :")
    print(features)
    print()
