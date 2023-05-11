import tkinter as tk

# tkinter title
root = tk.Tk()
root.title('title do tkinter')

# window 
# geometry é usado para definir o tamanho do programa
root.geometry('600x400+50+50')
root.resizable(False, False)

# isso vai deixar a tela transparente
root.attributes('-alpha', 0.5)


# tkinter loop run
root.mainloop()
