n = int(input("Tamanho do triangulo: "))

for i in range(1, n + 1):
    linha = ""
    for j in range(i):
        linha += "* "
    print(linha)
