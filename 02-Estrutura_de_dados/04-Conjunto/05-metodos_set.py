# União de conjunto
conjunto_a = {1,2,3,}
conjunto_b = {2,3,4,}
uniao = conjunto_a.union(conjunto_b)
print("União: ",uniao)

# Interceção no enter conjunto
print("----------------------------")
intercecao = conjunto_a.intersection(conjunto_b)
print("Interceção: ",intercecao)

# Tudo que tenho em um conjunto que nao tenho no outro incluindo a interceção
print("----------------------------") 
tem_nao_tem = conjunto_a.difference(conjunto_b)
print("Diferente: ",tem_nao_tem)

# Pegando todos os elementos que não estão nà interceção  
print("----------------------------")
nao_ta_na_intercecao = conjunto_a.symmetric_difference(conjunto_b)
print("Ñ está na interceção: ",nao_ta_na_intercecao)

# Esta contido não esta contido 
print("----------------------------")
conjunto_a = {1,2,3,}
conjunto_b = {4, 1, 2, 5, 6, 3,}

contidoA = conjunto_a.issuperset(conjunto_b)
contidoB = conjunto_b.issuperset(conjunto_a)
print(f"A: {conjunto_a} \nB: {conjunto_b}")
print("B esta contido em A: ",contidoA)
print("A esta contido em B: ",contidoB)

# Conjunto disjuntos nao tem elemento comuns entre eles 
print("----------------------------")
conjunto_a = {1,2,3,}
conjunto_b = {4,5,6,7,}
print(f"A: {conjunto_a} \nB: {conjunto_b}")
disjunto = conjunto_a.isdisjoint(conjunto_b)
print(f"Disjuntos: {disjunto}")

# Metodo adiciona se nao tiver o elemento ele adiciona 
print("----------------------------")
conjunto_a.add(25,)
print("Adicionando: ",conjunto_a)

# limpando 
conjunto_a.clear()

# copiando 
copiado = conjunto_b.copy()

# Descartando valors tambem tem o remove a diferenca é que o remove da um erro se nao tiver o elemento
print("----------------------------")
copiado.discard(5)
print("Descartando 3 de B: ",copiado ) 

# removendo valores da esquerda para a direita pop()
print("----------------------------")
copiado.pop()
print("Tirando o primeiro da pilha: ", copiado)

# Verificando o tamanho 
print(len(copiado)) 

# vento se tem um elemento 
print(7 in copiado)