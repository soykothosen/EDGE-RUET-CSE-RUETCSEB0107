import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Basic Widgets")
root.geometry("500x500")

# Add a label
label = tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 16))
label.pack(pady=20)

# Add a button
def on_button_click():
    label.config(text="Button Clicked!")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

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




# Run the application
root.mainloop()
