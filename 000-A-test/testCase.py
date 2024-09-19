class Veiculo:
    def __init__(self, cor):
        self.cor = cor
    def __str__(self):
            return f"{self.__class__.__name__}: {', '.join({f'{chave}={valor}' for chave, valor in self.__dict__.items()})}"

vaca = Veiculo('verde')
print(vaca)