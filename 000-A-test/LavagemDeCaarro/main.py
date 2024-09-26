from fun_carro import add, lista

# Menu
show = """
    1 - Cadastra
    2 - lista
    0 - Sair
"""


# lupe
while True:
    print(show)
    op = input('Opção: ')
   
    if op == '1':
       add()
        
    elif op == '2':    
        lista()
        
    elif op == '0':
        break
    