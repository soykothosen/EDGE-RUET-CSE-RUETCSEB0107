import tkinter as tk
from tkinter import messagebox

class LoginScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Screen")
        self.geometry("600x600")

        # Title label
        tk.Label(self, text="Login", font=("Arial", 24, "bold")).pack(pady=20)

        #Lebel 1
        self.label1 = tk.Label(self, text="Login1", font=("Arial", 24, "bold"))
        self.label1.pack(pady=2)

        # Mobile Number input
        tk.Label(self, text="Mobile Number:", font=("Arial", 14)).pack(pady=5)
        self.mobile_entry = tk.Entry(self, font=("Arial", 14), width=25)
        self.mobile_entry.pack(pady=5)

        # Password input
        tk.Label(self, text="Password:", font=("Arial", 14)).pack(pady=5)
        self.password_entry = tk.Entry(self, font=("Arial", 14), width=25, show="*")
        self.password_entry.pack(pady=5)

        

        # Login button
        tk.Button(self, text="Login", font=("Arial", 14), width=15, bg="blue", fg="white", command=self.logInClick).pack(pady=20)

        # Register button
        tk.Button(self, text="Register", font=("Arial", 14), width=15, bg="green", fg="white").pack(pady=20)

        

    def logInClick(self):
            print("Log In buton Click")
            #messagebox.showinfo("Error", "Both fields are required!")
            self.label1.config(text="Loading")
        


if __name__ == "__main__":
    app = LoginScreen()
    app.mainloop()
