
# Laco infinito
while True:
    
    opcao = input('Digite um numero = ')
    
    if opcao == "10":
        break
    
    print(opcao)
    
for numero in range(51):
    
    if numero % 2 == 0:
        continue
    print(numero,end=" ")
    