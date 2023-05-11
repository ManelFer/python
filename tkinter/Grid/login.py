import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("240x100")
        self.title("Login")
        self.resizable(0, 0)

        # configuração do grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self.create_widgets()

    def create_widgets(self):
        # username
        username_label = ttk.Label(self, text="username: ")
        username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        username_entry = ttk.Entry(self)
        username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        # password
        password_label = ttk.Label(self, text="password: ")
        password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        password_entry = ttk.Entry(self, show='*')
        password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # login
        login_label = ttk.Button(self, text="Login")
        login_label.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

if __name__=="__main__":
    app = App()
    app.mainloop()





