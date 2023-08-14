def palindromo(texto):
    texto_reverso = texto[::-1]  
    return texto == texto_reverso

arara = "arara"
nome = "Mateus"

print(palindromo(arara))  
print(palindromo(nome))  
