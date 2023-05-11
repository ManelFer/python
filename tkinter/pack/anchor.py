"""
A opção "anchor" permite ancorar o widget à borda do espaço 
alocado. Ela aceita um dos seguintes valores:
    Sticky	Description
    N	North or Top Center
    S	South or Bottom Center
    E	East or Right Center
    W	West or Left Center
    NW	North West or Top Left
    NE	North East or Top Right
    SE	South East or Bottom Right
    SW	South West or Bottom Left
    CENTER	Center

"""
import tkinter as tk
root = tk.Tk()
root.title("Anchor - tkinter")
root.geometry("350x200")

# box 1
box1 = tk.Label(root, text="box 1", bg="green", fg="white")
box1.pack(ipadx=20, ipady=20, anchor=tk.E, expand=True) # foi usado "anchor"

# box 2
box2 = tk.Label(root, text="box 2", bg="red", fg="white")
box2.pack(ipadx=20, ipady=20, anchor=tk.W, expand=True) # foi usado "anchor"

root.mainloop()