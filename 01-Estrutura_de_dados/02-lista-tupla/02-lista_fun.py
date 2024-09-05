
livro = [1,"Python","Way",30,40,50,30,"Way"]

# copiando lista 
lista = livro.copy()
print(id(lista), id(livro))

# contando quantas vezes algo se repete na lista
l1 = lista.count("Way")
print(l1)

# Colocando uma lista dentro de outra lista  ela não remove valores duplicados
lista.extend([50,'python'])
print(lista)

