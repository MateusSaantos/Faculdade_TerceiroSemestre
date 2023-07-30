minimo = 10
maximo = 1000

saque = int(input("Digite o valor do saque (múltiplo de 10, entre 10 e 1000): "))

if saque < minimo or saque > maximo or saque % 10 != 0:
    print("Valor inválido.")
else:
    notas_200 = saque / 200
    saque %= 200

    notas_100 = saque / 100
    saque %= 100

    notas_50 = saque / 50
    saque %= 50

    notas_10 = saque / 10

    print(f"Notas de 200: {notas_200}")
    print(f"Notas de 100: {notas_100}")
    print(f"Notas de 50: {notas_50}")
    print(f"Notas de 10: {notas_10}")
