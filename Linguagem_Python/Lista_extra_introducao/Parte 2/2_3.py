itros = float(input("Litragem: "))
combustivel = input("A = Alcool\nG = Gasolina: ")

gasolina = 4.20
alcool = 2.80
total = 0

if combustivel == "A" or combustivel == "a":
    if litros <= 20:
        total = litros * (alcool - (alcool * 0.03))
        print(f"Total: {total}")
    else:
        total = litros * (alcool - (alcool * 0.05))
        print(f"Total: {total}")
        
elif combustivel == "G" or combustivel == "g":
    if litros <= 20:
        total = litros * (gasolina - (gasolina * 0.04))
        print(f"Total: {total}")
    else:
        total = litros * (gasolina - (gasolina * 0.06))
        print(f"Total: {total}")