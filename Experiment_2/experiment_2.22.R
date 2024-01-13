# 加载必要的库
library(ggplot2)
library(RColorBrewer)

# 提供的数据
data <- data.frame(
  Date = rep(c("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"), each = 3),
  Year = rep(c(2013, 2014, 2015), times = 12),
  Value = c(0.371, 0.623, 0.7, 0.456, 0.8455, 0.95, 0.74, 0.95, 1, 0.5429, 0.7743, 0.89,
            0.5796, 0.7084, 0.92, 0.6862, 0.705, 0.94, 0.516, 0.645, 0.86, 0.472, 0.656, 0.8,
            0.4816, 0.7224, 0.86, 0.4418, 0.8178, 0.94, 0.3818, 0.6474, 0.83, 0.4617, 0.6075, 0.81)
)

# 选择RColorBrewer的颜色方案
my_colors <- brewer.pal(3, "Set1")  # 这里选择了Set1方案，你可以根据需要选择其他方案和颜色数量

# 创建玫瑰图并使用RColorBrewer颜色方案
p <- ggplot(data, aes(x = Date, y = Value, fill = as.factor(Year))) +
  geom_bar(stat = "identity", position = "stack", width = 1) +
  coord_polar() +
  theme_minimal() +
  scale_fill_manual(values = my_colors) +  # 使用RColorBrewer颜色
  labs(title = "Rose Diagram", fill = "Year")

# 显示图形
p
