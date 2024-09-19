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
foo.x = 10 
print(foo.x)