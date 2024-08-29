# Ordem de precedencia das Operação Matematicas 
"""
Parêntesis
Expoentes
Módulo 
Multiplicações e divisões (da esquerda para a direita)
Somas e Subtrações (da esquerda para a direita)


Parênteses (se houver)
Exponenciação (**)
Módulo (%)
Multiplicação e Divisão (* e /)
Adição e Subtração (+ e -)


"""  

produto_1 = 10
produto_2 = 20

print(produto_1 +produto_2)
# Retorna um valor negativo por que o 1 é menor que o 2
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 * produto_2)
# Modulo o resto da divisao de um número
print(produto_1 % produto_2)
print(produto_1 ** produto_2)

x = 9 % 2**8 -2 * 4
print(x)

y = (10 / 2 ) + (25 * 2) - (2 ** 2)
print(y)

y2 = (10 / 2 ) + 25 * ((2 - 2) ** 2)
print(y2)