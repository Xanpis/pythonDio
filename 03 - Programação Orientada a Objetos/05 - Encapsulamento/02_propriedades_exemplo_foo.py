class Foo:
    def __init__(self, x=None):
        self._x = x
        

    """
    Com o property eu posso criar atributos gerenciados ou computada ou seja quando precisar 
    modificar sua implementação  interna sem alterar a api publica da classe.
    A propriedade ela pega um método e transforma ele em uma propriedade  
    Aqui estou pegando x se tiver valor ele retorna se não retorne  0  
    """
    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        
        # essa  é uma maneira de trabalhar com porrete
        # _x = self._x or 0
        # _valor = value or 0
        # self._x = _x + _valor
        
        # Eu não posso usar o retorno nesse caso porque ele não é um método mas uma propriedade 
        # Return  self._x += value
        
        # Correto
         self._x += value

    @x.deleter
    def x(self):
        self._x = 0


foo = Foo(6)
foo.x = 10 # vai se agora 20
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)
