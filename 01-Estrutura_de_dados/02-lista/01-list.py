# O Python o metodo list vai colocar um valor de cada vez porque ele itera os valores 
letra = list("Python")
print(letra)

numeros = list(range(10 ))
print(numeros[9])

# lista com predation
numeros = [1, 21, 32, 40, 60,33,11]
pares = []

for nun in numeros:
    if nun % 2 ==0:
        pares.append(nun) 
print(pares)        