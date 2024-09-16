

class Bicicleta:
    """
    O que é o self, O self é uma referencia para o objeto, Uma referencia explicita,
    Outras linguagem se usa referencia implícita
    Pose ser outra palavra como this , Mas por convenção se ussa self. 
    O Que quer dizer que é uma instancia ao objeto
    """

class Bicicleta:

    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    
    # A forma de Declarar um método é ter sempre um self no inicio 
    # para ter um referencia explicita ao objeto



    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

        
        
    # Retornando o nome da classe
    def __str__(self):
        """ 
        Com o (self.__class__.__name_) eu estou pegando a instancia do meu objeto referenciado pelo self uma vez com a classe eu pego o nome
        Depois eu uso uma lista comprehension para pegar os valores dos atributos
        O __dict retorna um dicionario com chave e valor por isso itero com o intens()
        Depois eu tenho que transforma tudo  em texto com o .join() por que o comprehension me retorna uma lista
         
        """
    def __str__(self):

        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)
b2.correr()


# Referencia explicita 
b3 = Bicicleta("Marron", "Quadro de moça", 2005, 300)


