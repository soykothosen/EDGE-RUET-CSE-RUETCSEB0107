class Button:
    def __init__(self,color,shape):
        self.Color = color
        self.Shape = shape

    def buttonClick(self):
        print(self.Color+ " Button is Clicked")

class shadowButton(Button):
    def __init__(self, color, shape, shadow):
        super().__init__(color, shape)
        self.Shadow = shadow
        #self.Color = "Red"
    
    def hoverAlert(self):
        print("Thanks for hover")

buttons = shadowButton("Green","Rectangle","3 px")

print(buttons.Shape)
print(buttons.Color)
print(buttons.Shadow)
buttons.hoverAlert()

