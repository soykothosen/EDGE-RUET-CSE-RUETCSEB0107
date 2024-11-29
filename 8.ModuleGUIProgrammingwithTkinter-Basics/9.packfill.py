import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

# Create widgets
label1 = tk.Label(root, text="Fill X", bg="red")
label2 = tk.Label(root, text="Fill Y", bg="green")

# Pack widgets with fill options
label1.pack(fill="x")  # Expands horizontally
label2.pack(fill="y")  # Expands vertically

root.mainloop()
