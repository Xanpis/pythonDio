
def analise_vendas(vendas):
    
    media_vendas = 0
    total_vendas = 0
    for i in vendas:
        total_vendas += i
        
    media_vendas = total_vendas / len(vendas)
    
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
 
    entrada = input()
    
    lista_de_strings = entrada.split(',')
    vendas = list(map(int,lista_de_strings))
    
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))