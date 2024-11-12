import textwrap
# entrada = input()
# erro = entrada.split(',')
# vendas = list(map(int,[i for i in erro if i.strip()]))

# print(vendas)

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        
    def __str__(self):
        return f"""
                nome: {self.nome}
                idade: {self.idade}
            """    

def add():
    nome = input('Nome: ')
    idade = input('idade: ')
    conta = Pessoa(nome, idade)
    array.append(conta)
    
        
array = []
add()

for i in array:
    print(i)

print(array)
