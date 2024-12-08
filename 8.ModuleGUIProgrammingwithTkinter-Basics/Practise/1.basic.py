import tkinter as tn

myapp = tn.Tk()

myapp.title("My First Test Tkinter App")
myapp.geometry("540x540")

label = tn.Label(myapp, text="Welcome to Tkinter!", font=("Arial", 16))
label.pack(pady=20)

lebel1 = tn.Label(myapp, text="Hi", font=("Arial", 16))
lebel1.pack()

label3 = tn.Label(myapp,
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
)

label3.pack()

def buttonClick():
    print("Button Click")
    lebel1.config(text="Button Clicked")

button1 = tn.Button(myapp,text="Log", command=buttonClick)
button1.pack(pady=20)

#input field
entry = tn.Entry(myapp)
entry.pack(pady=10)

#text box
text = tn.Text(myapp, height=5, width=30)
text.pack(pady=10)

#check button
var = tn.IntVar()
check = tn.Checkbutton(myapp, text="Check me!", variable=var)
check.pack(pady=10)






myapp.mainloop()