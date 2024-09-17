class Animal:
    def __init__(self, nro_patas ):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    """" 
     Se ussa o **kw quando eu tenho valores que se repetem no construtor da classe errada, 
     Quando eur tenho dois valore em classes diferentes e quero passar 3 argumentos o python
     nao indene para onde passar esse argumentos por isso eu uso o **kws que assim 
     eu tenho que passar os argumentos nomeados com chave e valor.
    """
    def __init__(self, cor_pelo , **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico , **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero):
    pass

# Conceito de mixin eu coloco o mixin na classe ela executa o Método que tem que executar e pronto 
class Maxim:
    def falando(self):
        return 'Estou falando'
    


class Ornitorrinco(Mamifero, Ave, Maxim) :
    def __init__(self, cor_bico , cor_pelo , nro_patas ):
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)
        # python __mro__ (ordem de resolução dos métodos) é a ordem que os métodos são reouvidos dentro da classe 
        # Se eu tiver outro método str dentro de Mamífero a execução para por ali por causa da ordem de execução 
        # como Mamífero é o que executa primero o retorno faz a execução parar ali 
        print(Ornitorrinco.__mro__)

"""
  Também pode ser desse jeito 
  
class Ornitorrinco(Mamifero, Ave):
    def __init__(self, **kw):
        super().__init__(**kw)
        
"""


gato = Gato(nro_patas=2,cor_pelo='verde')
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)
print(ornitorrinco.falando())