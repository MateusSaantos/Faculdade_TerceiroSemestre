salario = float(input("Salario: "))

if salario <= 1903.98:
    aliquota = 0
    deducao = 0
elif salario <= 2826.65:
    aliquota = 7.5
    deducao = 142.80
elif salario <= 3751.05:
    aliquota = 15.0
    deducao = 354.80
elif salario <= 4664.68:
    aliquota = 22.5
    deducao = 636.13
else:
    aliquota = 27.5
    deducao = 869.36

imposto = (salario * aliquota / 100) - deducao

print(f"Imposto: {imposto}")
