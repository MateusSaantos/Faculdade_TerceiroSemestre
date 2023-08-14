def converte(dias, horas, minutos, segundos):
    total = dias * 24 * 60 * 60 + horas * 60 * 60 + minutos * 60 + segundos
    return total

dias = 1
horas = 1
minutos = 1
segundos = 10

tempo = converte(dias, horas, minutos, segundos)
print("Tempo total em segundos:", tempo)
