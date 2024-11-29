import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

# Create widgets
label1 = tk.Label(root, text="Left", bg="red")
label2 = tk.Label(root, text="Right", bg="green")
label3 = tk.Label(root, text="Bottom", bg="blue")

# Pack widgets with side options
label1.pack(side="left")  # Packs to the left
label2.pack(side="right")  # Packs to the right
label3.pack(side="bottom")  # Packs to the bottom

root.mainloop()
