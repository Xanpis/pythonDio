# União de conjunto
conjunto_a = {1,2,3,}
conjunto_b = {2,3,4,}
uniao = conjunto_a.union(conjunto_b)
print("União: ",uniao)

# Interceção no enter conjunto
intercecao = conjunto_a.intersection(conjunto_b)
print("Interceção: ",intercecao)

# Tudo que tenho em um conjunto que nao tenho no outro incluindo a interceção 
tem_nao_tem = conjunto_a.difference(conjunto_b)
print("Diferente: ",tem_nao_tem)

# Pegando todos os elementos que não estão nà interceção  
nao_ta_na_intercecao = conjunto_a.symmetric_difference(conjunto_b)
print("Ñ está na interceção: ",nao_ta_na_intercecao)