import tkinter as tk

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
        # This is where you would add logic to save user information
        print(f"Name: {self.name_entry.get()}")
        print(f"Mobile: {self.mobile_entry.get()}")
        print(f"University: {self.university_entry.get()}")
        print(f"Password: {self.password_entry.get()}")

    def go_to_login(self):
        # Navigate to the login screen
        self.controller.show_frame("LoginScreen")
