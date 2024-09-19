# Set um conjunto de objetos que tem elemento unicos
# O set não suporta indexação buscar o valor na posicao  

# Eliminando valores duplicados de uma lista 
numeros = [1, 1, 1, 2, 2, 3, 3,]
uni = set(numeros)
print(uni)

# Eliminando Duplicados de um iterável
uni = set("abacaxi")
print(sorted(uni))

# Declarando um set 
sete7 = {"abacaxi","melao","manga","melao",}
print(sete7)

# como percorre uma lista 
for chave, valor  in  enumerate(sete7):
    print(f" {chave} : {valor} ",end= " | ") 
