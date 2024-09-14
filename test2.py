from datetime import datetime, date, time, timezone, tzinfo
from time import strptime

# datas_horas = datetime.now()
# print(datas_horas.strftime("%H:%M"))
# person = {}
# while True:

#     nome = input("nome: ")
#     person[nome] = ""
#     print(person)

#     if nome == "0":
#         break

def analise_vendas(vendas):
    # TODO: Calcule o total de vendas e realize a média mensal:
    media_vendas = 0
    total_vendas = 0
    for i in vendas:
        total_vendas += i
        
    media_vendas = total_vendas / len(vendas)
    
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de inteiros:
    lista_de_strings = entrada.split(',')
    vendas = list(map(int,lista_de_strings))
    
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))