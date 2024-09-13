
from datetime import datetime, date, time
import textwrap

# datas_horas_agora = datetime.now()
# mascara_data_BR = " %d/%m/%y " 
# mascara_hora = " %H:%M "
# data = datas_horas_agora.strftime(mascara_data_BR)  
# hora = datas_horas_agora.strftime(mascara_hora)


def menu():
    menu = f"""

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo Usuário
    [5] Criar conta
    [6] Lista conta
    [9] Sair

    => """
    return input(textwrap.dedent(menu))


# Adicionar usuário no banco
def user(user:list):   
    try:
        cpf = int(input(f"informe o CPF (somente números): "))
        usu = filtra_user(cpf, user)    
    except:
        print("Apenas números ")
        return
           
    if usu:
        print("Usuário Já Existe!!")
        return
    
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento: ")
    ender= input("Endereço: ")
    
    user.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": ender})
    print("Usuário Criado ")

# Criando conta para user
def criar_conta(agencia,numero_conta,user):
    try:
        cpf = int(input(f"informe o CPF (somente números): "))
        usu = filtra_user(cpf, user)         
    except:
        print("Apenas números ")
        return    
        
    if usu:
        print("Conta criada")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario":usu}
    print("Usuário não encontrado")

# Filtrando user    
def filtra_user(cpf,user):
    filtra_user = [us for us in user if us["cpf"] == cpf]
    return filtra_user[0] if filtra_user else None
 
# Função de deposito com argumento por posição
def depositar(saldo, extrato, var,/):
    if var > 0: 
        data_hora= datetime.now()
        saldo += var
        # extrato += f"Deposito: R${var:.2f}\tData: {data_hora.strftime("%d/%m/%y")}\tHora:{data_hora.strftime("%H:%M")}\n"
        extrato += f'Dep:\tR$ {var:.2f}\tData:{data_hora.strftime(" %d/%m/%y ")}\tHora:{data_hora.strftime(" %H:%M ")}\n'
        print("Adicionado")        
    else:
        print(f"Digite um valor maior que {var}")   
        
    return saldo,extrato     
       
#  Função sacar com argumentos nomeados
def sacar(*,saldo, extrato,limite,numero_saques, LIMITE_SAQUES, var):
  
    
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
            extrato += f'Saque: \tR$ {var:.2f}\tData:{data_hora.strftime(" %d/%m/%y ")}\tHora:{data_hora.strftime(" %H:%M ")}\n'   
        else:
            print("Saldo insuficiente")

    else:
        print(f"Digite um valor maior que {var}")          
    return saldo, extrato,numero_saques

# Função Extrato de forma posicional e nomeada 
def extrato_conta(extrato,/,*,saldo,numero_saques):
    
    print("         Extrato de transações")
    print("------------------------------------- ")
    print("Não tem operações na sua conta" if not extrato else extrato)
    print("------------------------------------- \n")
    print(f"Saldo: R$ {saldo:.2f}")
    print(f"Numero de saques: {numero_saques}")
    print("------------------------------------- \n")
 
def lista_conta(contas):
    for con in contas:
        linha = f"""
            Agencia:\t{con['agencia']}
            C/C:\t\t{con['numero_conta']}
            Titular:\t{con['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
    
def main():
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    pessoas = []
    contas = []
    AGENCIA = "0001"
    
    while True:
        op = menu()
        
        # Depositar
        if op == "1":
            try:
                var = float(input('Valor a ser depositado = R$ '))
                saldo,extrato = depositar(saldo,extrato,var)
            except:
                print("Erro de operação")
                
        # Sacar        
        elif op == "2":
            try:
                var = float(input("Valor a ser sacado: = R$ "))
                saldo, extrato,numero_saques = sacar(
                    saldo = saldo,
                    extrato = extrato,
                    limite = limite,
                    numero_saques = numero_saques,
                    LIMITE_SAQUES = LIMITE_SAQUES,
                    var = var,
                )
            except:
                print("Erro de operação")
                    
        # Extrato          
        elif op == "3":
            extrato_conta(
                 extrato,
                saldo = saldo,
                numero_saques = numero_saques
            )
        
        # Adicionar usuário
        elif op == "4":
            user(pessoas)

        # Criar conta
        elif op == "5":
            # O numero da conta do usario sempre vai aumentando em 1
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA,numero_conta,pessoas)
           
            if conta:
                contas.append(conta)    
       
        elif op == "6":
            lista_conta(contas)
       
        # Sair
        elif op == "9":
            print('Obrigado!!!')
            break
        
        else:
            print("Opção invalida")
            
main()

