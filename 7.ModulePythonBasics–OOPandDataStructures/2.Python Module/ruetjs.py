class Button:
    def __init__(self,color,shape):
        self.Color = color
        self.Shape = shape
    
    def buttonClick(self):
        print(self.Color+" button Clicked Shape "+ self.Shape)

class FormField:
    def __init__(self,inputtype,borderradius,bordercolor):
        self.inputType = inputtype
        self.borderRadius = borderradius
        self.borderColor = bordercolor

    def OnCursor(self):
        print(self.inputType+" Input Type Cursor Active")


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
