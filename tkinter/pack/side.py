"""
A opção 'side' especifica o alinhamento do seu widget
    .tkinter.TOP
    .tkinter.LEFT
    .tkinter.RIGHT
    .tkinter.BOTTOM
"""

import tkinter as tk
root = tk.Tk()
root.title("side - tkinter")
root.geometry("350x200")

# box 1
box1 = tk.Label(root, text="box 1", bg="green", fg="white")
box1.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side=tk.LEFT)

# box 2
box2 = tk.Label(root, text="box 2", bg="red", fg="white")
box2.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side=tk.RIGHT)

root.mainloop()