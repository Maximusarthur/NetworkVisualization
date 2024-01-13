import numpy as np

data_points = np.array([[-1.0000, -0.5000, 0.0000, 0.5000, 1.0000],
                        [0.1285, 0.2410, 0.3508, 0.3990, 0.3532]])

point_P = np.array([-0.4000, 0.2000])

# 计算曼哈顿距离
manhattan_distances = np.sum(np.abs(data_points - point_P.reshape(2, 1)), axis=0)

# 计算欧几里得距离
euclidean_distances = np.sqrt(np.sum((data_points - point_P.reshape(2, 1))**2, axis=0))
all_data_points = np.hstack((data_points, point_P.reshape(2, 1)))

# 计算均值μ
mean_estimate = np.mean(all_data_points, axis=1)[0]

print("曼哈顿距离:", manhattan_distances)
print("欧几里得距离:", euclidean_distances)
print("均值估计(μ):", mean_estimate)
