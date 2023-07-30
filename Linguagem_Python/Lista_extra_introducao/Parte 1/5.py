area = float(input("Digite o tamanho em metros quadrados: "))

litros = area / 3
if area % 3 != 0:
    litros += 1

latas = int(litros / 18)
if litros % 18 != 0:
    latas += 1

total = latas * 80

print(f"Latas de tinta necessarias: {latas}")
print(f"Valor total: {total}")

