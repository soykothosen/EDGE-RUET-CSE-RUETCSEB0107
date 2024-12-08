import tkinter as tk
from login_screen import LoginScreen
from registration_screen import RegistrationScreen

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login and Registration Example")
        self.geometry("400x400")
        
        # Create a container for frames
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        
        self.frame_login = LoginScreen(parent=self.container, controller=self)
        self.frame_registration = RegistrationScreen(parent=self.container, controller=self)

        # Store frames manually in a dictionary
        self.frames = {
            "LoginScreen": self.frame_login,
            "RegistrationScreen": self.frame_registration
        }

        # Stack frames on top of each other using grid
        self.frame_login.grid(row=0, column=0, sticky="nsew")
        self.frame_registration.grid(row=0, column=0, sticky="nsew")

        # Show the login screen initially
        self.show_frame("LoginScreen")

    def show_frame(self, frame_name):
        """Show the frame by name."""
        frame = self.frames[frame_name]
        frame.tkraise()  # Raise the selected frame to the front

if __name__ == "__main__":
    app = App()
    app.mainloop()
