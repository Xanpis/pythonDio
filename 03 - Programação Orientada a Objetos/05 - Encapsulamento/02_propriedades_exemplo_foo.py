class Foo:
    def __init__(self, x=None):
        self._x = x

    """
    Com o property eu posso criar atributos gerenciados ou computada ou seja quando precisar 
    modificar sua implementação  interna sem alterar a api publica da classe.
    Aqui estou pegando x se tiver valor ele retorna o valor, ou 0  
    """
    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        _x = self._x or 0
        _valor = value or 0
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0


foo = Foo(10)
print(foo.x)
foo.x = 10 # vai se agora 20
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)
