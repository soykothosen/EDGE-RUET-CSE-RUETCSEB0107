import tkinter as tk

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Frame Example")
        self.geometry("400x300")

        # Create a frame
        frame = tk.Frame(self)
        frame.pack(fill="both", expand=True)  # Pack the frame to the window

        # Add widgets inside the frame
        label = tk.Label(frame, text="This is a Label inside the Frame", font=("Arial", 14))
        label.pack(pady=10)

        button = tk.Button(frame, text="Click Me", command=self.on_button_click)
        button.pack(pady=10)

    def on_button_click(self):
        print("Button Clicked!")

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
