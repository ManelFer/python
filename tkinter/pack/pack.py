"""
IpadX cria um preenchimento à esquerda e à direita, ou seja
um preenchimento ao longo do eixo X

IpadY cria um preenchimento superior e inferior, ou seja, um
preenchimento ao longo do eixo Y

"tkinter.X" - preenche o espaço disponivel ao longo do eixo x
"tkinter.Y" - preenche o espaço disponivel ao longo do eixo y
"tkinter.BOTH" - preenche o espaço disponivel ao longo de ambos os eixos

Quando você usa a opção "fill", a área que cada widget pode preencher
é limitada pela áreas alocadas a eles.

" EXPAND "
""" 

import tkinter as tk
root = tk.Tk()
root.title('Pack Demo - tkinter')
root.geometry("350x200")

# box 1
box1 = tk.Label(root, text="box 1", bg="green", fg="white")
box1.pack(ipadx=10, ipady=10, fill=tk.X) # ativar a box. Agora vou usar o "fill"

# box 2
box2 = tk.Label(root, text="box 2", bg="red", fg="white")
box2.pack(ipadx=10, ipady=10)


root.mainloop()