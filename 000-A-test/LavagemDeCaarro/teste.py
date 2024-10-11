class Car:
    def __init__(self,name) -> None:
        self.name = name
    
    def __str__(self) -> str:
        return __class__.__name__

u = Car('Fulano')
print(u)