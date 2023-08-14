def calcular_potencia(base, expoente):
    resultado = base ** expoente
    return resultado

base = float(input("Base: "))
expoente = int(input("Expoente: "))

resultado = calcular_potencia(base, expoente)

print("Resultado:", resultado)
