# (*) Recebe uma tuple 
# (**) Recebe um Dicionario  

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n ".join(args)
    meta_dados = "\n ".join([f"{chave.title()}:{valor}" for chave, valor in  kwargs.items()])
    mensagem = f"\n\n{data_extenso}\n\n {texto}\n\n {meta_dados}"
    print(mensagem)
    
exibir_poema(
    "sexta 26 de agosto de 2022",
    "Zen of Python",
    "Beautiful is better than ugly",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    autor="Tim Peters",
    ano=1999,
)
    
    
