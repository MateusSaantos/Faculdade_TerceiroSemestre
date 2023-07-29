- Códigos usados na linguagem R para tarefa:

dados=c(48,55,47,50,57,52,49,50,51,45,44,45,49,54,46,43,49,50,56,50,47,48,37,52,53,53,57,52,54,50)
length(dados)

#Ordenar vetor:
dados = sort(dados)
print(dados)

#Quartis:
quantile(dados, type=6)

#BoxPlot
library("qboxplot")
qboxplot(data.frame(dados),horizontal=TRUE,qtype=6)

#Histograma sem parâmetros:
hist(dados,right=FALSE)

#Histograma com adicionais:
hist(dados, breaks=seq(20, 80, l=15))

