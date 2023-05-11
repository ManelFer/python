import tkinter as tk

root = tk.Tk()
root.title('Tkinter center - window')

window_width = 300
window_height = 300

# obter as dimensões da tela
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# definir o ponto central
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# definir a posição da janela no centro da tela
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# loop para iniciar o programa
root.mainloop()