setwd("D:/Workspace_TI/CE/forest-fire")
getwd()
data = read.csv("ForestFireModel_model_data_iter_300_steps_60_2023-01-20-14-58-01.836718.csv")
data
str(data)
library(ggplot2)
ggplot(data) +
  geom_histogram(mapping = aes(x = arvores_irrecuperaveis))
ggplot(data) + 
  geom_point(aes(y=arvores_irrecuperaveis, x=health_percentage))
ggplot(data, mapping = aes(y=arvores_recuperaveis, x=health_percentage)) +
  geom_boxplot()
ggplot(data) +
  geom_count(mapping = aes(y=arvores_recuperaveis, x=health_percentage))
ggplot(data, mapping = aes(y=arvores_recuperaveis, x=health_percentage)) + 
  geom_boxplot(mapping = aes(group = cut_width(health_percentage, 0.1)))
