# 加载必要的库
library(ggplot2)
library(RColorBrewer)

# 创建数据框
dt <- data.frame(A = c(2, 7, 4, 10, 1, 6, 8, 3), B = c('B', 'A', 'C', 'D', 'E', 'F', 'G', 'H'))

# 绑定特定字体
windowsFonts(myFont = windowsFont("楷体"))

# 使用RColorBrewer创建新的配色方案
my_colors <- brewer.pal(8, "Set1")

# 创建极区图并修改配色方案
p <- ggplot(dt, aes(x = B, y = A, fill = B)) +
  geom_bar(stat = "identity", alpha = 0.7) +
  coord_polar() +
  scale_fill_manual(values = my_colors)  # 设置新的配色方案

# 显示图形
p
