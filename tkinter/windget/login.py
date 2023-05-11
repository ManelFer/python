import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Login tkinter')
root.geometry('300x200')
root.resizable(False, False)

# adicionar o email 
email = tk.StringVar()
password = tk.StringVar()

def login_clicked():
    """ callback when the login button clicked
    """
    msg = f'You entered email: {email.get()} and password: {password.get()}'
    showinfo (
        title='Information',
        message=msg
    )

# sign in frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)

# email
email_label = ttk.Label(signin, text='Email address: ')
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email, )
email_entry.pack(fill='x', expand=True)
email_entry.focus()

# password
password_label = ttk.Label(signin, text="Password")
password_label.pack(fill='x', expand=True)

# deixar a senha secreta
password_entry = ttk.Entry(signin, textvariable=password, show="*")
password_entry.pack(fill='x', expand=True)

# login button
login_button = ttk.Button(signin, text="Login", command=login_clicked)
login_button.pack(fill='x', expand=True, pady=10)
# loop para iniciar o programa
root.mainloop()