import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

# Create widgets
label1 = tk.Label(root, text="Label with Padding", bg="red")

# Add padding around the label
label1.pack(padx=20, pady=40)

root.mainloop()
