from abc import ABC, abstractmethod, abstractproperty

# Como usar uma interface corretamente importar os módulos e coloque os Decoradores 
# quando eu falo que minha classe é ABC eu não posso mais instanciá-la
class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

# Forçando a implementação de uma propriedade
    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    
# Agora eu sou obrigado a definir os dois methods
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
