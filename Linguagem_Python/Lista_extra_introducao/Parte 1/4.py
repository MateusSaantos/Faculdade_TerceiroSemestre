salario = float(input("Salario: "))
horas = float(input("Horas trabalhadas: "))

bruto = salario * horas
imposto = 0.15 * bruto
inss = 0.10 * bruto
sindicato = 0.02 * bruto
liquido = bruto - imposto - inss - sindicato

print("Salario Bruto: ", bruto)
print("Imposto de Renda: ", imposto)
print("INSS: ", inss)
print("Sindicato: ", sindicato)
print("Liquido: ", liquido)
