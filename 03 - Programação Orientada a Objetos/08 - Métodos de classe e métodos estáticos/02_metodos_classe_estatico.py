
"""
Todos são Método veiculados a classe e não a instancia da classe.
Quando  usar métodos de classe = Quando eu quero criar métodos de fabrica 
Quando  usar métodos estático = Geralmente usado para criar funções utilitária

"""
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    # Diferença è que  no método de classe primeiro parâmetro aponta para classe o método estático não.
    # O método de classe pode acessar ou modificar o estado da classe, o estático não.. por que não ? 
    # porque ele não tem a referencia para fazer esse acesso 
    # o class retorna um nova estancia da classe pessoa
    
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)
    

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    

p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
