
def analise_vendas(vendas):
    # TODO: Calcule o total de vendas e realize a média mensal:
    media_vendas = 0
    total_vendas = 0
    for i in vendas:
        total_vendas += i
        
    media_vendas = total_vendas / len(vendas)
    
    return f"{total_vendas}: {media_vendas:.2f}"

def obter_entrada_vendas():
    entrada = input()
 
    # TODO: Converta a entrada em uma lista de inteiros:
    lista_de_strings = entrada.split(',')
    
    # No Map eu  passo o tipo que vai ser convertido e a lista e ele me retorna um objeto do tipo map 
    # Então eu uso a lista para converter para lista 
    vendas = list(map(int,lista_de_strings))
    
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))