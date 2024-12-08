import tkinter as tk
import json

class RegistrationScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        label = tk.Label(self, text="Registration Screen", font=("Arial", 16))
        label.pack(pady=20)

        # Name
        self.name_label = tk.Label(self, text="Name")
        self.name_label.pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        # Mobile Number
        self.mobile_label = tk.Label(self, text="Mobile Number")
        self.mobile_label.pack()
        self.mobile_entry = tk.Entry(self)
        self.mobile_entry.pack()

        # University
        self.university_label = tk.Label(self, text="University")
        self.university_label.pack()
        self.university_entry = tk.Entry(self)
        self.university_entry.pack()

        # Password
        self.password_label = tk.Label(self, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        # Register Button
        register_button = tk.Button(self, text="Register", command=self.register)
        register_button.pack(pady=10)

        # Go to Login Button
        login_button = tk.Button(self, text="Go to Login", command=self.go_to_login)
        login_button.pack()

    def register(self):
        """Register a new user and save data in the JSON file."""
        name = self.name_entry.get()
        mobile = self.mobile_entry.get()
        university = self.university_entry.get()
        password = self.password_entry.get()

        # Load existing users data from JSON file
        with open('user_data.json', 'r') as file:
            data = json.load(file)
            users = data["users"]

        # Add new user to the list
        new_user = {
            "name": name,
            "mobile": mobile,
            "university": university,
            "password": password
        }
        users.append(new_user)

        # Save updated data back to JSON file
        with open('user_data.json', 'w') as file:
            json.dump(data, file, indent=4)

        # Show registration success and go to login screen
        success_label = tk.Label(self, text="Registration Successful!", fg="green")
        success_label.pack(pady=10)
        self.controller.show_frame("LoginScreen")

    def go_to_login(self):
        """Navigate to the login screen."""
        self.controller.show_frame("LoginScreen")
