import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

# Create widgets
label1 = tk.Label(root, text="Label 1", bg="red")
label2 = tk.Label(root, text="Label 2", bg="green")

# Pack widgets with expand options
label1.pack(fill="both", expand=True)  # Expands in both directions
label2.pack(fill="both", expand=True)  # Expands in both directions

root.mainloop()
