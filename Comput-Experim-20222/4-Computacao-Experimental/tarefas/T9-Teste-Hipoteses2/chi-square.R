# pacote R para facilitar a transformação de dados intervalares em dados categóricos
install.packages("DescTools")
library(DescTools)

# lendo as amostras
library(readr)
todas_as_amostras <- read_csv("model_data_iter_150_steps_100_2022-03-31 21-02-41.015965.csv")

# analisando os valores únicos para as variáveis independentes dos experimentos
unique(todas_as_amostras$density)
unique(todas_as_amostras$wind)

# controlando as amostras para a densidade fixa de 0.65

amostras_controladas_pela_densidade_065 <- todas_as_amostras[todas_as_amostras$density==0.65,]

# vendo os valores máximo e mínimo das amostras controladas

max(amostras_controladas_pela_densidade_065$`Number of clusters (Fine)`)
min(amostras_controladas_pela_densidade_065$`Number of clusters (Fine)`)

# criando uma faixa de intervalos para segmentar os dados de `Number of clusters (Fine)`

faixa_de_corte <- c(17,31,47,63)

# criando variáveis categóricas a partir de dados intervalares discretos 

wind48 <- Freq(amostras_controladas_pela_densidade_065$"Number of clusters (Fine)"[amostras_controladas_pela_densidade_065$wind==48],breaks=faixa_de_corte)
wind48

wind43 <- Freq(amostras_controladas_pela_densidade_065$"Number of clusters (Fine)"[amostras_controladas_pela_densidade_065$density==0.65 & a$wind==43],breaks=faixa_de_corte)
wind43

# Criando e observando uma tabulação cruzada entre os dados categóricos de ventos fortes e ventos fracos
crosstable <- as.table(rbind(wind43$freq, wind48$freq))
crosstable

# Dado nomes mais compreensíveis às linhas e colunas da tabela
dimnames(crosstable) <- list(vento=c("Fraco","Forte"),fragmentacao=c("Alta","Média","Baixa"))
crosstable

# Fazendo o teste do chi-square
chisq.test(crosstable)
