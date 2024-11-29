import tkinter as tk
import os
import json
from login_screen import LoginScreen
from registration_screen import RegistrationScreen
from profile_screen import ProfileScreen

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login and Registration with Profile")
        self.geometry("400x400")

        # Check if the 'user_data.json' file exists, if not create it
        self.check_create_user_data_file()

        # Create a container for frames
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Initialize frames manually
        self.frame_login = LoginScreen(parent=self.container, controller=self)
        self.frame_registration = RegistrationScreen(parent=self.container, controller=self)
        self.frame_profile = None  # Profile screen will be created dynamically

        # Store frames in a dictionary
        self.frames = {
            "LoginScreen": self.frame_login,
            "RegistrationScreen": self.frame_registration
        }

        # Stack frames on top of each other using grid
        self.frame_login.grid(row=0, column=0, sticky="nsew")
        self.frame_registration.grid(row=0, column=0, sticky="nsew")

        # Show the login screen initially
        self.show_frame("LoginScreen")

    def check_create_user_data_file(self):
        """Check if the user_data.json file exists, if not, create it."""
        file_path = 'user_data.json'
        print(f"Saving file at: {os.path.abspath(file_path)}")
        
        if not os.path.exists('user_data.json'):
            # Create an empty JSON structure for user data
            initial_data = {"users": []}
            with open('user_data.json', 'w') as file:
                json.dump(initial_data, file, indent=4)

    def show_frame(self, frame_name, user_data=None):
        """Show the frame by name and pass user data to profile."""
        if frame_name == "ProfileScreen" and user_data:
            self.frame_profile = ProfileScreen(self.container, self, user_data)
            self.frame_profile.grid(row=0, column=0, sticky="nsew")
            self.frames["ProfileScreen"] = self.frame_profile
        else:
            frame = self.frames[frame_name]
            frame.tkraise()  # Raise the selected frame to the front

if __name__ == "__main__":
    app = App()
    app.mainloop()
