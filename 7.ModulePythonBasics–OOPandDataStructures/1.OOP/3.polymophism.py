class Button:
    def __init__(self, color, shape):
        self.Color = color
        self.Shape = shape

    def Click(self):
        print("Button Click")


class Link:
    def __init__(self, linktextColor):
        self.Color = linktextColor
    
    def Click(self,type):
        self.Type = type
        if self.Type == "New Tab":
            print("Link Open in New Tab")
        else:
            print("Link Open in Current Tab")

class Image:
    def __init__(self):
        pass
    
    def Click(self, type):
        self.Type = type
        if self.Type == "New Tab":
            print("Link Open in New Tab")
        else:
            print("Link Open in Current Tab")


button1 = Button("Red","Circle")
link1 = Link("Green")
image1 = Image()

print(button1.Color);
print(link1.Color)

button1.Click()
link1.Click("New Tab")
image1.Click("New Ta")


        