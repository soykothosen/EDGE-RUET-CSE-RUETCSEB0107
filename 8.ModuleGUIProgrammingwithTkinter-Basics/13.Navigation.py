import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Navigation Example")
        self.geometry("400x300")

        # Create a container for frames
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Dictionary to store frames
        self.frames = {}
        print(self.frames)  

        # Initialize frames
        for F in (Frame1, Frame2):
            frame = F(parent=self.container, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # Stack frames on top of each other


        print(self.frames)    


        self.show_frame(Frame1)  # Start with Frame1

        

    def show_frame(self, frame_class):
        """Bring the frame to the front."""
        frame = self.frames[frame_class]
        frame.tkraise()  # Raise the selected frame to the front


class Frame1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="This is Frame 1", font=("Arial", 16))
        label.pack(pady=20)

        button = tk.Button(self, text="Go to Frame 2",
                           command=lambda: controller.show_frame(Frame2))
        button.pack()


class Frame2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="This is Frame 2", font=("Arial", 16))
        label.pack(pady=20)

        button = tk.Button(self, text="Go to Frame 1",
                           command=lambda: controller.show_frame(Frame1))
        button.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
