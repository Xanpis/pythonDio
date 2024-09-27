
class Foo:
    def __init__(self, x=None):
        self._x = x

    def x(self):
        return self._x 
    
       
    def x(self, value):
        self._x += value


    def x(self):
        self._x = 0


foo = Foo(10)
print(foo.x)
# só estou modificando o apontamento da memoria e não o seu valor 
foo.x 
print(foo.x)