import ruetjs

button1 = ruetjs.Button("Red","Rectangle")
button1.buttonClick()


link1 = ruetjs.Link("Blue")
link1.Click("New")


class MyStyleButton(ruetjs.Button):
    def __init__(self, color, shape, textstyle):
        super().__init__(color, shape)
        self.textStyle = textstyle

    def hoverClick(self):
        print("Hover Clicked")

newbutton = MyStyleButton("Blue","Triangle","Italic")

newbutton.hoverClick()
print(newbutton.textStyle)