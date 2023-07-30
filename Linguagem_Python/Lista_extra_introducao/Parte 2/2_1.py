peso = float(input("Peso em kg: "))
altura = float(input("Altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"Seu IMC é: {imc}")
    print("Você está abaixo do peso.")
elif imc >= 18.5 and imc <= 25.0:
    print(f"Seu IMC é: {imc}")
    print("Você está com peso normal.")
else:
    print(f"Seu IMC é: {imc}")
    print("Você está com sobrepeso.")