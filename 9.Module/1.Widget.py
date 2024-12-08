import tkinter as tk
from tkinter import messagebox 

# Create the main window
root = tk.Tk()
root.title("Basic Widgets")
root.geometry("500x500")

# Add a label
labelr = tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 16))
labelr.pack(pady=0)

#messagebox.showinfo("showinfo", "Information") 
messagebox.showwarning("showwarning", "Warning") 

# Add a button
def on_button_click():
    labelr.config(text="Button Clicked!")

a = tk.Button(root, text="Click Me", command=on_button_click)
a.pack(pady=10)

#input field
entry = tk.Entry(root)
entry.pack(pady=10)

#text box
text = tk.Text(root, height=5, width=30)
text.pack(pady=10)

#check button
var = tk.IntVar()
check = tk.Checkbutton(root, text="Check me!", variable=var)
check.pack(pady=10)

button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()

tk.Button(root, text='Stop', width=25, command=root.destroy).pack(pady=10)




# Run the application
root.mainloop()
