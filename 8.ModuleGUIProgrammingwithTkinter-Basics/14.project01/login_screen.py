import tkinter as tk

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
        # This is where you would add logic to validate user credentials
        print(f"Mobile: {self.mobile_entry.get()}")
        print(f"Password: {self.password_entry.get()}")

    def go_to_registration(self):
        # Navigate to the registration screen
        self.controller.show_frame("RegistrationScreen")
