
def produto_mais_vendido(produtos):
    contagem = {}
    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1
    
    max_produto = {}
    max_count = 0
    
    for produto, count in contagem.items():
        if count > max_count:
            max_count = count
            max_produto[produto] = max_count            
    
    return contagem, max_produto

def obter_entrada_produtos():
  
    entrada = input()
    # TODO: Converta a entrada em uma lista de strings, removendo espaços extras:
    lista_de_strings = entrada.split(',')
    
    produtos = [s.strip() for s in lista_de_strings if s.strip()]
    return produtos

produtos = obter_entrada_produtos()
cont, maxi = produto_mais_vendido(produtos)
print(f"""      
    Todos = {cont}  
    
    Máximo = {maxi}   
    """)

()