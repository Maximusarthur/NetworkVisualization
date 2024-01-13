import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.ensemble import RandomForestRegressor

# 网格步长和边距
mesh_size = .02
margin = 0

# 加载鸢尾花数据集
df = px.data.iris()

# 选择特征和目标变量
X = df[['sepal_width', 'sepal_length']]
y = df['petal_width']

# 使用RandomForestRegressor模型进行训练
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# 创建一个网格用于运行模型
x_min, x_max = X.sepal_width.min() - margin, X.sepal_width.max() + margin
y_min, y_max = X.sepal_length.min() - margin, X.sepal_length.max() + margin
xrange = np.arange(x_min, x_max, mesh_size)
yrange = np.arange(y_min, y_max, mesh_size)
xx, yy = np.meshgrid(xrange, yrange)

# 运行模型进行预测
pred = model.predict(np.c_[xx.ravel(), yy.ravel()])
pred = pred.reshape(xx.shape)

# 生成3D散点图
fig = px.scatter_3d(df, x='sepal_width', y='sepal_length', z='petal_width')
fig.update_traces(marker=dict(size=5))
fig.add_traces(go.Surface(x=xrange, y=yrange, z=pred, name='pred_surface'))
fig.show()
