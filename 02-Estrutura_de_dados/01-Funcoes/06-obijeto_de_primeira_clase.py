# Funcoes tambem são objetos de primeira classe

def somar(c,d):
    return c + d 

def diminuir(c,d):
    return c - d 

def exibir_resultado(a, b, fun ):
    var = fun(a,b)
    return print(f"O Resultado é = {var}")

# Tenho que passar a funcao sem colchetes 
exibir_resultado(10,10 , somar)

exibir_resultado(10,10 , diminuir)

op = somar
print(op(20,40))
