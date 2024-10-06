class Pessoa:
    def __init__(self, nome = None, idade = None):
        self.nome = nome
        self.idade = idade
    
    
    def criar_de_data_nascimento(self, ano, mes, dia, nome):
        idade = 2022 - ano
        # Retornando para a instancia da minha classe
        return Pessoa (nome, idade)
    
    # Jeito correto, assim eu instancio minha classe apenas um vez, referenciando minha classe com o classmethod
    # @classmethod
    # def criar_de_data_nascimento(cls, ano, mes, dia, nome):
    #     idade = 2022 - ano
    #     return cls(nome, idade)
    
# Quando eu tenho esse comportamento de instanciar minha classe duas veze para 
# Mudar seu comportamento eu uso o classmethod    
p = Pessoa().criar_de_data_nascimento(1997,3,22,"Furão")

print(p.nome, p.idade)