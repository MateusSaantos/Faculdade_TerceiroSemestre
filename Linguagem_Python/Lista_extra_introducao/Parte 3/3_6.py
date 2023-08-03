numero = int(input("Digite um número inteiro: "))

if numero < 2:
    print("O número não é primo.")
else:
    primo = True
    divisores = []

for i in range(2, int(numero ** 0.5) + 1):
    if numero % i == 0:
        primo = False
        divisores.append(i)

if primo:
    print("O número é primo.")
else:
    print("O número não é primo. É divisível por:", divisores)