from fun_carro import add, lista,remover

# Menu
show = """
[1] Cadastra 
[2] Listar 
[3] Remover 
[4] Sair
"""


# lupe1

while True:
    print(show)
    op = input('Opção:')
   
    if op == '1':
       add()
        
    elif op == '2':    
        lista()
        
    elif op == '3':    
        remover()
        
    elif op == '0':
        break
        