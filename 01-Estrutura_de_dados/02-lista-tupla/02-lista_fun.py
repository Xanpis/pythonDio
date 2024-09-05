
from traceback import print_tb


livro = [1,"Python","Way",30,40,50,30,"Way"]

# copiando lista 
lista = livro.copy()
print(id(lista), id(livro))

# contando quantas vezes algo se repete na lista
l1 = lista.count("Way")
print(l1)

# vendo o tamanho da lista 
l1 = len(lista)
print(l1)

# Colocando uma lista dentro de outra lista  ela não remove valores duplicados
lista.extend([50,'python'])
print(lista)

# Encontrando o objeto de primeira ocorrencia 
l2 = lista.index(30)
print(lista[3])
print(l2)

# Tirando o ultimo elemento da pilha ou com o indice do elemento
lista.pop()
print(lista) 
lista.pop(2)
print(lista)

# Removendo o objeto sem o indice, remove a primeira ocorrencia 
lista.remove(30)
print(lista)

# Colocando lista ao Contrario
lista.reverse()
print(lista)

# Ordenando a lista com sort
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)