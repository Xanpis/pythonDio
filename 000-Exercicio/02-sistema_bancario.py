from datetime import datetime, date, time

# datas_horas_agora = datetime.now()
# mascara_data_BR = " %d/%m/%y " 
# mascara_hora = " %H:%M "
# data = datas_horas_agora.strftime(mascara_data_BR)  
# hora = datas_horas_agora.strftime(mascara_hora)


menu = f"""

[1] Depositar
[2] Sacar
[3] Extrato
[4] Adiciona Usuário
[5] Lista usuário
[9] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
person = {}


# Adicionar usuário no banco
def user(nome):
    person[nome] = ""
    print("Adicionado")
    
# Função de deposito
def depositar(var):
    global saldo,extrato
    
    if var > 0: 
        data_hora= datetime.now()
        saldo += var
        extrato += f"Deposito: R$ {var:.2f} Data:{data_hora.strftime(" %d/%m/%y ")} Hora:{data_hora.strftime(" %H:%M ")} \n"
    else:
        print(f"Digite um valor maior que {var}")        
   
#  Função sacar
def sacar(var):
    global saldo, extrato,limite,numero_saques,LIMITE_SAQUES
    
    if var > 0: 
        if numero_saques == LIMITE_SAQUES:
            print("Limite de saque atingido volte amanhã !!")
        
        elif var > limite:
            print(f"Valor acima do limite R$ {limite}")        
                
        elif saldo >= var:
            data_hora= datetime.now()
            saldo -= var
            numero_saques += 1
            print('Dinheiro Sacado')      
            extrato += f'Saque: R$ {var:.2f} Data:{data_hora.strftime(" %d/%m/%y ")} Hora:{data_hora.strftime(" %H:%M ")}\n'   
        else:
            print("Saldo insuficiente")

    else:
        print(f"Digite um valor maior que {var}")  

# Função Extrato
def extrato_conta():
    
    print("         Extrato de transações")
    print("------------------------------------- ")
    print("Não tem operações na sua conta" if not extrato else extrato)
    print("------------------------------------- \n")
    print(f"Saldo: R$ {saldo:.2f}")
    print(f"Numero de saques: = {numero_saques}")
    print("------------------------------------- \n")


while True:
    op = input(menu)
    
    # Depositar
    if op == "1":
        try:
            var = float(input('Valor a ser depositado = R$ '))
            depositar(var)
        except:
            print("Erro de operação")
            
    # Sacar        
    elif op == "2":
        try:
            var = float(input("Valor a ser sacado: = R$ "))
            sacar(var)
        except:
            print("Erro de operação")
                 
    # Extrato          
    elif op == "3":
        extrato_conta()
    
    # Adicionar usuário
    elif op == "4":
        name = input("Qual seu nome: ")
        user(name)

    # Listar usuario
    elif op == "5":
        if not person:
            print("Não tem usuário")
        else:   
            for i,v in enumerate(person, start=1):
                print(f"{i}: {v}")
            
    # Sair
    elif op == "9":
        print('Obrigado!!!')
        break
    
    else:

        print("Opção invalida")