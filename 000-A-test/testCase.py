class Veiculo:
    def __init__(self, cor):
        self.cor = cor
    def __str__(self):
            return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Carro(Veiculo):
    def __init__(self,cor,lugares):
            super().__init__(cor)
            self.lugares = lugares



"""
Quando eu instício meu objeto o python não intende para qual construtor eu devo passar o segundo argumento
para isso eu tenho o **kw, quando eu adiciono ele no construtor,
eu tenho que passar no parâmetro do objeto instanciado chave e valor

"""   
carro_4x4 = car_4x4 (cor='verde', lugares= 4, capacidade_de_carga = "200kg" )