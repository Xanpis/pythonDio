
entrada = input()
erro = entrada.split(',')
vendas = list(map(int,[i for i in erro if i.strip()]))

print(vendas)