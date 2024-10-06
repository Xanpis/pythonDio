saldo = 1000
saque = 200
limite = 100

# verdade e verdade == verdade
if saldo >= saque and saque <= limite:
    print("Sacando Dinheiro")
else:
    print("Valor Incorreto")
 
# verdade ou falso == falso   
if saldo >= saque or saque <= limite:
    print("Sacando Dinheiro")
else:
    print("Valor Incorreto")

# Negando o falso vira verdadeiro  
x = not 100 > 1500
print(x)

# lista vazia em python é falsa então retorna true     
contatos_emergencia = [] 
print(not contatos_emergencia)