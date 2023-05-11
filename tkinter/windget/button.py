import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('tkinter - button')
root.geometry('300x300+50+50')

# botão tkinter
exite_button = ttk.Button(
    root,
    text='Exite',
    command=lambda: root.quit()
)

exite_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
# loop para iniciar o programa
root.mainloop()