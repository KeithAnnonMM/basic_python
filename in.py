class Car:
    name = ''
    model = ''
    color = ''

    def __init__(self,model,name,color):
        self.model = model
        self.name = name
        self.color = color

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def setModel(self,model):
        self.model = model

    def getModel(self):
        return self.model

    def setColor(self,color):
        self.color = color

    def getColor(self):
        return self.color

    def checkCarDetails(self):
        print(self.getName())
        print(self.getColor())
        print(self.getModel())

class RangeRover(Car):
    pass

range_rover = RangeRover('2012','Range Rover Evogue','Black')
range_rover.checkCarDetails()
