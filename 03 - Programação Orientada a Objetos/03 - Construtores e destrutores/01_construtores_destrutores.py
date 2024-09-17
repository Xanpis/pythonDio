class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    # Desalocando memoria do objeto criado quando eu termino de instanciar o objeto o del apaga. 
    # O python também faz isso de forma Automática sem precisar do dell
    def __del__(self):
        print("Removendo a instância da classe.")


    def falar(self):
        print("auau")


def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)


c = Cachorro("Chappie", "amarelo")
c.falar()
print("Ola mundo")
print("Ola mundo")

# O método dander __del__  da classe só remove no final aqui eu estou forcando uma remoção
del c

print("Ola mundo")
print("Ola mundo")
