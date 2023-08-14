def numeros_positivos(lista):
    positivos = []
    for numero in lista:
        if numero > 0:
            positivos.append(numero)
    return positivos

valores = [1, 2, -23, -1]
lista = numeros_positivos(valores)
print("Positivos:", lista)
