import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

# Create widgets
label1 = tk.Label(root, text="Label 1", bg="red")
label2 = tk.Label(root, text="Label 2", bg="green")
label3 = tk.Label(root, text="Label 3", bg="blue")

# Pack widgets
label1.pack(pady=10)  # Default: top
label2.pack()  # Default: top
label3.pack()  # Default: top

root.mainloop()
