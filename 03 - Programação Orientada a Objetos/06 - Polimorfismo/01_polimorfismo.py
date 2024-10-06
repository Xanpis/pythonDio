
# A palavra polimorfismo significa muitos formas, Ou seja voce pose ter os mesmos métodos mas coma assinatura deferente 
class Passaro:
    def voar(self):
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")
    # é uma maneira de referenciar a classe pai diretamente, 
    # permitindo que você chame seus métodos sem precisar mencionar o nome da classe
        return super().voar()
    

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")


# NOTE: exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")


# Com o self que é a referencia da classe também fucina Mas é melhor aplicado dentro da classe
def plano_voo(obj):
    obj.voar()


plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
