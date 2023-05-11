import tkinter as tk
root = tk.Tk()
root.title("Tudo que aprendi - tkinter")
root.geometry("350x200")

# criar uma variavel para representar o ipadx e o ipady
ipadding = {'ipadx': 10, 'ipady': 10}

# adicionar as box
box1 = tk.Label(root, text="box 1", bg="red", fg="white")
box1.pack(**ipadding, fill=tk.X)

box2 = tk.Label(root, text="box 2", bg="green", fg="white")
box2.pack(**ipadding, fill=tk.X)

box3 = tk.Label(root, text="box 3", bg="blue", fg="white")
box3.pack(**ipadding, fill=tk.X)

# box que vai ficar em baixo
box4 = tk.Label(root, text="box 4", bg="cyan", fg="black")
box4.pack(**ipadding, expand=True, fill=tk.BOTH, side=tk.LEFT)

box5 = tk.Label(root, text="box 5", bg="magenta", fg="black")
box5.pack(**ipadding, expand=True, fill=tk.BOTH, side=tk.LEFT)

box6 = tk.Label(root, text="box 6", bg="yellow", fg="black")
box6.pack(**ipadding, expand=True, fill=tk.BOTH, side=tk.LEFT)


# ativar o programa
root.mainloop()