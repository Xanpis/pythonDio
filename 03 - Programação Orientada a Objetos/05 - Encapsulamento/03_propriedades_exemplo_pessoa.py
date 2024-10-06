class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento
        
        
    # NOTE : Se eu não tenho regra de NEGOCIO para validar ou modificar, eu não preciso do property 
    # é mas a carra do python chamas a atributo diretamente quando for publico...
    @property
    def name(self):
        return self.nome
    

    # A qui eu preciso porque estou validando algo privado
    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento


pessoa = Pessoa("Guilherme", 1994)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
    