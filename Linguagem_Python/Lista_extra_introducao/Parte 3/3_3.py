numeros = []
contador = 0
soma = 0

while contador < 5:
    numero = float(input(f"Digite o número {contador + 1}: "))
    numeros.append(numero)
    soma += numero
    contador += 1

media = soma / contador

print("Soma:", soma)
print("Média:", media)
