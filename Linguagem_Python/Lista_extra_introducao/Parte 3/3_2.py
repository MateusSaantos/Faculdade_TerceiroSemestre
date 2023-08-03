numeros = []

for i in range(5):
    numero = float(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

maior_numero = numeros[0]

for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero

print("O maior número é:", maior_numero)