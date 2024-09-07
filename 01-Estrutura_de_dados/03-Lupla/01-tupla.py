# # Diferenca de tuple e lista: tuple é um objeto imutavel 
from itertools import count


frutas = ("laranja","manga","uva","melao",) # Sempre adicionar uma , no final
print(frutas)

# Iteravel
frutas2 = tuple("Python") 
print(frutas2)

numeros = tuple([1,2,3,4]) # Passando numeros
print(numeros)

tu = ('p', 'y', 't', 'h', 'o', 'n' , 7,7,)
print(tu)
print(tu[2:6])

print(len(tu))
print(tu.count('y')) 
 
print(tu.index(7))
