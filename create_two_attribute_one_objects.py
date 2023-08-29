from create_one_attribute import Person

#create an object named "person" whose name is "Ali", age is "25"

class Person:
    def  __init__(self,name,age) -> None:
        self.name=name
        self.age=age
x=Person('Ali','25')
print(x.name,x.age)

