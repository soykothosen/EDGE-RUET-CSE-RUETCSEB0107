class Person:
    height = 6
    color = "Black"

p = Person() #p Object

print(p.height)
print(p.color)



class Person1:
    def __init__(self, height, color):
        self.jeight = height
        self.Color = color
    
    def Hello(self):
        print("Hi Hello " + self.Color)

    def Hello1(self,name):
        self.Name = name
        print("Hi Hello " + self.Name)

p1 = Person1(8,"Black") # p1 Object

print(p1.jeight)
print(p1.Color)
p1.Hello()
p1.Hello1("Soykot")