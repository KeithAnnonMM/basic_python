class Animal:
    def __init__(self,type):
        self.type = 'Keith'


class Lion(Animal):
    name = 'Simba'
    age = 0

    def __init__(self,name,age,type):
        self.type = type
        self.name = name
        self.age = age

lion1 = Lion('Livaro',20,'Carnivo')
print(lion1.type)