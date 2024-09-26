from fun_carro import add, lista,remover

# Menu
show = """
    1 - Cadastra 
    2 - lista 
    3 - Remover 
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
        
    elif op == '3':    
        remover()
        
    elif op == '0':
        break
    