import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import spearmanr

# 数据集
data = {
    'group1': {'X': [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0],
               'y': [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]},
    'group2': {'X': [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0],
               'y': [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]},
    'group3': {'X': [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0],
               'y': [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]},
    'group4': {'X': [8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 19.0, 8.0, 8.0, 8.0],
               'y': [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]}
}

# 计算均值
means_X = {group: np.mean(values['X']) for group, values in data.items()}
means_y = {group: np.mean(values['y']) for group, values in data.items()}

# 计算方差
variances_X = {group: np.var(values['X'], ddof=1) for group, values in data.items()}
variances_y = {group: np.var(values['y'], ddof=1) for group, values in data.items()}

# 计算Spearman相关系数
correlation_coefficients = {group: spearmanr(values['X'], values['y']).correlation for group, values in data.items()}

# 打印结果
for group in data.keys():
    print(f"Group {group}:")
    print(f"  Mean X: {means_X[group]:.2f}")
    print(f"  Mean y: {means_y[group]:.2f}")
    print(f"  Variance X: {variances_X[group]:.2f}")
    print(f"  Variance y: {variances_y[group]:.2f}")
    print(f"  Spearman Correlation Coefficient: {correlation_coefficients[group]:.2f}")
    print()

# 绘制散点图
for group, values in data.items():
    plt.scatter(values['X'], values['y'], label=group)

plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
