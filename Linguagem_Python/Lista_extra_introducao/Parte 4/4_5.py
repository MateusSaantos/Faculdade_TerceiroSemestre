def ocorrencias(palavra, caracter):
    contador = 0
    for letra in palavra:
        if letra == caracter:
            contador += 1
    return contador

palavra = "arara"
caracter = "r"
ocorrencias = ocorrencias(palavra, caracter)
print("A")
print("Ocorrencias: ", ocorrencias)
