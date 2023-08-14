def mdc(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


numero1 = int(input("Digite valor: "))
numero2 = int(input("Digite o segundo valor: "))

mdc = mdc(numero1, numero2)

print("MDC: ", mdc)
