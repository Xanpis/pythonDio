
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    op = input(menu)
    
    # Depositar
    if op == "d":
        var = float(input('Valor a ser depositado = R$ '))
        
        if var > 0: 
            saldo += var
            extrato += f"Valor depositado = R$ {var:.2f} \n"
        else:
            print(f"Digite um valor maior que {var}")        
            
    # Sacar        
    elif op == "s":
        var = float(input("Valor a ser sacado: = R$ "))
        
        if var > 0: 
        
            if numero_saques == LIMITE_SAQUES:
                print("Limite de saque atingido volte amanhã !!")
            
            elif var > limite:
                print(f"Valor acima do limite informe um valor abaixo ou igual R$ {limite}")
                
                    
            elif saldo >= var:
                saldo -= var
                numero_saques += 1
                print('Dinheiro Sacado')   
                extrato += f'saque: {numero_saques}\n'   
                extrato += f'Dinheiro Sacado: R$ {var:.2f}\n'   
                
            else:
                print("Valor saque maior do que o valor na conta ")
                
        else:
            print(f"Digite um valor maior que {var}")        
            
    # Extrato          
    elif op == "e":
        print("         Extrato de transações")
        print("------------------------------------- ")
        print("Não tem operacoes na sua conta" if not extrato else extrato)
        print("------------------------------------- \n")
        print(f"Saldo: R$ {saldo:.2f}")
        print(f"Numero de saques: = {numero_saques}")
        print("------------------------------------- \n")
    
    elif op == "q":
        print('Obrigado!!!')
        break
    
    else:
        print("Opção invalida")
    