import tkinter as tk

class ProfileScreen(tk.Frame):
    def __init__(self, parent, controller, user_data):
        super().__init__(parent)
        self.controller = controller
        self.user_data = user_data
        
        label = tk.Label(self, text="Profile Screen", font=("Arial", 16))
        label.pack(pady=20)

        # Display User Profile Information
        name_label = tk.Label(self, text=f"Name: {self.user_data['name']}")
        name_label.pack()

        mobile_label = tk.Label(self, text=f"Mobile: {self.user_data['mobile']}")
        mobile_label.pack()

        university_label = tk.Label(self, text=f"University: {self.user_data['university']}")
        university_label.pack()

        # Logout Button
        logout_button = tk.Button(self, text="Logout", command=self.logout)
        logout_button.pack(pady=10)

    def logout(self):
        """Log out and return to the login screen."""
        self.controller.show_frame("LoginScreen")
