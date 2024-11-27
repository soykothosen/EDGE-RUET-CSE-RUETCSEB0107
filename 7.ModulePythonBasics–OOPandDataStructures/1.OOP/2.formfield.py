class FormField:
    def __init__(self,inputtype,borderradius,bordercolor):
        self.inputType = inputtype
        self.borderRadius = borderradius
        self.borderColor = bordercolor

    def OnCursor(self):
        print(self.inputType+" Input Type Cursor Active")


textfield = FormField("text",0,"black")

textfield.OnCursor()

class myCustomFormField(FormField):
    def __init__(self, inputtype, borderradius, bordercolor,fillcolor, shadow):
        super().__init__(inputtype, borderradius, bordercolor)
        self.fillColor = fillcolor
        self.Shadow = shadow
        #self.inputType = fillcolor
    
    def OnHover(self):
        print(self.inputType+" Button on Hover")


emailfield = myCustomFormField("email","2 px", "Red", "Green", "0 px")

emailfield.OnHover()
emailfield.OnCursor()
print(emailfield.inputType)
