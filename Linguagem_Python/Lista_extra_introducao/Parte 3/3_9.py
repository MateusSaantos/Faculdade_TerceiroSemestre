A = []
B = []
C = []
D = []
E = []

while True:
    nota = float(input("Digite uma nota (-1 para sair): "))
    
    if nota == -1:
        break  
    
    if nota >= 9.0 and nota <= 10.0:
        A.append(nota)
        
    elif nota >= 8.0 and nota < 9.0:
        B.append(nota)
        
    elif nota >= 7.0 and nota < 8.0:
        C.append(nota)
        
    elif nota >= 6.0 and nota < 7.0:
        D.append(nota)
        
    elif nota >= 0.0 and nota < 6.0:
        E.append(nota)
        
    else:
        print("Nota invalida!")
    
# Exibindo as listas de notas
print("A:", A)
print("B:", B)
print("C:", C)
print("D:", D)
print("E:", E)
