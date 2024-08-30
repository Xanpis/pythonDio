"""
Ele é composto por 3 partes 
1 - Retorno se a condição for verdadeira
2 - A expressão logica 
3 - Retorno caso a expressão não seja atendida   

"""

saldo = 500
valor = 501
status  = "Sucesso" if saldo >= valor else "Saldo insuficiente" 

print(status)
