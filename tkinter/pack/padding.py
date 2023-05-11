"""
Para definir os preenchimentos externos dos widgets, você usa 
os parâmetros "padx" e "pady":
    .padx - preenche o espaço disponivel ao longo do eixo x
    .pady - preenche o espaço disponivel ao longo do eixo y
"""

import tkinter as tk
root = tk.Tk()
root.title("padding - tkinter")
root.geometry("350x200")

# box 1
box1 = tk.Label(root, text="box 1", bg="green", fg="white")
box1.pack(ipadx=20, ipady=20, padx=20, pady=20, fill=tk.BOTH, expand=True)

# box 2
box2 = tk.Label(root, text="box 2", bg="red", fg="white")
box2.pack(ipadx=20, ipady=20, padx=20, pady=20, fill=tk.BOTH, expand=True)


root.mainloop()