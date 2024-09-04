# O Python o metodo list vai colocar um valor de cada vez porque ele itera os valores 
letra = list("Python")
print(letra)

numeros = list(range(10 ))
print(numeros[9])


lista = ['P', 'y', 't', 'h', 'o', 'n']

print(lista[2:]) # ['t', 'h', 'o', 'n'] 0 ,1 a frente 
print(lista[:2]) # ['P', 'y'] 2-1 = 0, 1


# lista sem comprehension
numeros = [1, 21, 32, 40, 60,33,11]
pares = []

for nun in numeros:
    if nun % 2 ==0:
        pares.append(nun) 
print(pares)        

# lista sem comprehension
numeros = [1, 21, 32, 40, 60,33,11]
pares = [num for num in numeros if num % 2 == 0]
print(pares,'com_pre')

# Elevando ao quadrado 
quadrado = [ i ** 2 for i in numeros]
print(quadrado)