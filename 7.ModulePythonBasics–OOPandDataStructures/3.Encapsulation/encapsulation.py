#Public

class FirstButton:
    def __init__(self,color,shape):
        self.Color = color
        self.Shape = shape
    
    def buttonClick(self):
        print(self.Color+" button Clicked Shape "+ self.Shape)


button1 = FirstButton("Green","Circle")

print(button1.Color)
button1.Color = "Red"
print(button1.Color)


#Private
class SecondButton:
    def __init__(self,color,shape):
        self.__Color = color #double Under Score Here
        self.__Shape = shape #double Under Score Here
    
    def getColor(self): #Getter
        #logic here
        return self.__Color
    
    def setColor(self,newColor): #Setter
        #logic here
        self.__Color = newColor
    
    
    def __buttonClick(self):
        print(self.__Color+" button Clicked Shape "+ self.__Shape)

    def runButtonClick(self):
        #logic here
        self.__buttonClick()


button2 = SecondButton("Blue","Square")
#print(button2.__Color)
print(button2.getColor())
button2.setColor("Danger")
print(button2.getColor())
#button2.buttonClick()
button2.runButtonClick()


#Protected

class ThirdButton:
    def __init__(self,color,shape):
        self._Color = color  #Single Under Score Here
        self._Shape = shape  #Single Under Score Here
    
    def buttonClick(self):
        print(self._Color+" button Clicked Shape "+ self._Shape)


button3 = ThirdButton("Green","Circle")

print(button3._Color)
button3._Color = "Red"
print(button3._Color)

#Why Protected (Suggest)

class ForthButton:
    def __init__(self,color,shape):
        self._Color = color  #Single Under Score Here
        self._Shape = shape  #Single Under Score Here
    
    def buttonClick(self):
        print(self._Color+" button Clicked Shape "+ self._Shape)


class ModifyForthButton(ForthButton):
    def __init__(self, color, shape, size):
        super().__init__(color, shape)
        self.Size = size
    
    def AccessColor(self):
        return self._Color
    
    def changeColor(self,NewColor):
        self._Color = NewColor
    

button4 = ModifyForthButton("Custom","Circle","Small")

print(button4.Size)
print(button4.AccessColor())
button4.changeColor("Navy Blue")
print(button4.AccessColor())