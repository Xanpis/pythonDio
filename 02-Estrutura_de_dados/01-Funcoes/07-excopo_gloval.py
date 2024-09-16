"""
Não é recomendado usar escopo global
apenas se precisar no condigo
 
"""

salario = 2000

def salario_bonus(bonus, lista_test:list):
    global salario
    salario += bonus
    # eu tambem estou mudando a variavel (lista) por referencia 
    lista_test.append(45)
    # É a mesma coisa que isso 
    lista.append(70)
    return salario
    
lista = [1]

print(salario_bonus(200, lista))

# funciona para lista porque lista é imutavel, tudo de operacao eu altero por referencia. 
print(lista)

# Maneira correta
def salario_bonus2 (bonus,lis:list):
    global salario

    # Fazendo uma copia da lista
    lista_aux = lis.copy()
    lista_aux.append(5)
    print(f"lista_aux:{lista_aux}")
    
    salario += bonus
    return salario

salario_bonus2(900, lista)

