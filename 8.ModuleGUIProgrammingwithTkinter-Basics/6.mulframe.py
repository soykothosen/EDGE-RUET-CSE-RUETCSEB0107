import tkinter as tk

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Multiple Frames Example")
        self.geometry("400x300")

        # Create a frame for the top section (e.g., a title or header)
        header_frame = tk.Frame(self, bg="green")
        header_frame.pack(fill="x", pady=10)

        # Add a label to the header frame
        header_label = tk.Label(header_frame, text="Welcome to My App", font=("Arial", 18))
        header_label.pack()

        # Create a frame for the body section
        body_frame = tk.Frame(self, bg="red")
        body_frame.pack(fill="both", expand=True)

        # Add a button to the body frame
        body_button = tk.Button(body_frame, text="Click Me", command=self.on_button_click)
        body_button.pack(pady=20)

        # Create a frame for the footer section
        footer_frame = tk.Frame(self, bg="green")
        footer_frame.pack(fill="x", pady=10)

        # Add a label to the footer frame
        footer_label = tk.Label(footer_frame, text="Footer Section", font=("Arial", 12))
        footer_label.pack()

    def on_button_click(self):
        print("Button Clicked!")

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
