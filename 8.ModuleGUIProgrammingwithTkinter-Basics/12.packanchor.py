import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

# Create widgets
label1 = tk.Label(root, text="Anchored Label", bg="red")

# Anchor the label to the northwest (top-left corner)
label1.pack(anchor="nw")

root.mainloop()
