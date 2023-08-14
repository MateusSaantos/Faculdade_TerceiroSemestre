def contar(texto):
    vogais = ['a', 'e', 'i', 'o', 'u']
    contador = 0
    for letra in texto.lower():
        if letra in vogais:
            contador += 1
    return contador

texto = "Alemanha"
total = contar(texto)
print("Vogais: ", total)
