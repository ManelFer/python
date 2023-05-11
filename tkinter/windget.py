import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# label tkinter
tk.Label(root, text='classic label').pack()
ttk.Label(root, text='Themed label').pack()

# root para iniciar o programa
root.mainloop()
