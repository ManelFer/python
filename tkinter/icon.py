import tkinter as tk

root = tk.Tk()
root.title('Tkinter - icon')
root.geometry('300x300+50+50')
root.resizable(False, False)

#root para mudar o icon
root.iconbitmap('./tkinter/teste.icon')

# root para iniciar o programa
root.mainloop()