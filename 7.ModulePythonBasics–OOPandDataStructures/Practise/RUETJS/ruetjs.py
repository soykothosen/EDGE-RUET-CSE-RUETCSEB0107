class Button:
    def __init__(self,color,shape):
        self.Color = color
        self.Shape = shape

    def buttonClick(self):
        print(self.Color+ " Button is Clicked")

class Link:
    def __init__(self,linkcolor):
        self.LinkColor = linkcolor
    
    def Click(self,type):
        self.Type = type

        if self.Type == "New Tab":
            print("Open Url in New Tab")
        else:
            print("Open Url in Curret Tab")