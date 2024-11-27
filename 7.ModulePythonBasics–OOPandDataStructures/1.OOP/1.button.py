class Button:
    def __init__(self,color,shape):
        self.Color = color
        self.Shape = shape
    
    def buttonClick(self):
        print(self.Color+" button Clicked Shape "+ self.Shape)


button1 = Button("Green","Round")

print(button1.Color)
print(button1.Shape)
button1.buttonClick()

button2 = Button("Red","Rectangle")

print(button2.Color)
print(button2.Shape)
button2.buttonClick()
        