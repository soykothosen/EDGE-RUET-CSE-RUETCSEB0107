import tkinter as tk
import json
import os


class LoginScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        label = tk.Label(self, text="Login Screen", font=("Arial", 16))
        label.pack(pady=20)

        # Mobile Number
        self.mobile_label = tk.Label(self, text="Mobile Number")
        self.mobile_label.pack()
        self.mobile_entry = tk.Entry(self)
        self.mobile_entry.pack()

        # Password
        self.password_label = tk.Label(self, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        # Login Button
        login_button = tk.Button(self, text="Login", command=self.login)
        login_button.pack(pady=10)

        # Go to Registration Button
        register_button = tk.Button(self, text="Go to Registration", command=self.go_to_registration)
        register_button.pack()

    def login(self):
        """Validate the login credentials."""
        mobile = self.mobile_entry.get()
        password = self.password_entry.get()

        # Check if the file exists and print a debug message
        if not os.path.exists('user_data.json'):
            print("File 'user_data.json' not found!")
        else:
            print("File 'user_data.json' exists.")


        # Load users from the JSON file
        with open('user_data.json', 'r') as file:
            data = json.load(file)
            users = data["users"]
            print(users)

        # Check if the credentials match
        for user in users:
            if user["mobile"] == mobile and user["password"] == password:
                # Successfully logged in, show the profile screen
                self.controller.show_frame("ProfileScreen", user)
                return

        # If login fails, show an error message
        error_label = tk.Label(self, text="Invalid mobile or password", fg="red")
        error_label.pack(pady=10)

    def go_to_registration(self):
        """Navigate to the registration screen."""
        self.controller.show_frame("RegistrationScreen")
