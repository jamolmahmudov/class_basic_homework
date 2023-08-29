#Create a "Person" class
class Person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
x = Person('Ali','15')
print(x.age)