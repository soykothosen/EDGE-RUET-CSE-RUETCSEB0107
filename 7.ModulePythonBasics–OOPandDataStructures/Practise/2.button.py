class Button:
    def __init__(self,color,shape):
        self.Color = color
        self.Shape = shape

    def buttonClick(self):
        print(self.Color+ " Button is Clicked")

button1 = Button("Green","Square")

print(button1.Color)
print(button1.Shape)
button1.buttonClick()
