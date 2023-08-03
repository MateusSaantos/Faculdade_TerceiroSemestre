
nome = input("NOME: (maior que 3 caracteres): ")
while len(nome) <= 3:
    nome = input("Nome inválido. Digite novamente (maior que 3 caracteres): ")

idade = int(input("IDADE: (entre 0 e 150): "))
while idade < 0 or idade > 150:
    idade = int(input("Idade inválida. Digite novamente (entre 0 e 150): "))

salario = float(input("SALARIO (maior que zero): "))
while salario <= 0:
    salario = float(input("Salário inválido. Digite novamente (maior que zero): "))

sexo = input("SEXO \nF - Feminino\nM - Masculino: ").upper()
while sexo != "F" and sexo != "M":
    sexo = input("Sexo inválido. Digite novamente \nF - Feminino\nM - Masculino: ")

estado_civil = input("ESTADO CIVIL: \nS - Solteiro\nC - Casado\nV - Viuvo\nD - Divorciado: ")
while estado_civil != "S" and estado_civil != "C" and estado_civil != "V" and estado_civil != "D":
    estado_civil = input("Estado civil inválido. Digite novamente \nS - Solteiro\nC - Casado\nV - Viuvo\nD - Divorciado: ")

print("NOME:", nome)
print("IDADE:", idade)
print("SALARIO:", salario)
print("SEXO:", sexo)
print("ESTADO CIVIL:", estado_civil)

