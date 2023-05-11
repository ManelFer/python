"""
A opção "expand" aloca mais espaço disponivel para o widget. Se
você adicionar a opção "expand" ao primeiro widget no caso a box 1.

 Neste ex, o primeiro widget ocupa todo o espaço disponivel n jenale,
exceto pelo espaço alocado ao segundo widget.
 Como o primeiro widget não tem a opção "fill", ele flutua no meio 
da área alocada.
 Se você definir a opção "fill" do primeiro widget como tk.BOTH. line 19.
"""

import tkinter as tk
root = tk.Tk()
root.title("Expand - tkinter")
root.geometry("350x200")

# box 1
box1 = tk.Label(root, text="box 1", bg="green", fg="white")
box1.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True)

# box 2 
box2 = tk.Label(root, text="box 2", bg="red", fg="white")
box2.pack(ipadx=20, ipady=20, expand=True)

root.mainloop()