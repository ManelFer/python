import tkinter 
from tkinter import messagebox


root = tkinter.Tk()
root.withdraw()

count = 0

msg_box = messagebox.showwarning("Tomo PAPUDO!", "VOCÊ FOI HACKEADO")

if msg_box ==  'ok' :
    msg_box = messagebox.showwarning("PERA AI!", "PARA SER DESHACKEADO PRECISO QUE RESPONDA UMA PERGUNTA...")

if msg_box == 'ok':
    msg_box = messagebox.askquestion("O QUE ACHA?", "ACEITA NAMORAR COMIGO?")

while msg_box == 'no':
    count +=1
    msg_box = messagebox.askquestion("O QUE ACHA?", "ACEITA NAMORAR COMIGO?")
    if (count == 1000000000):
        msg_box = messagebox.showerror("TO INDO AI!", "VOU TE DAR UNS CASCUDOS")
        break

if msg_box == 'yes':
    msg_box = messagebox.showinfo("BOA ESCOLHA!", "SABIA QUE IA FAZER UMA OTIMA ESCOLHA")
    #reproduzir musica
