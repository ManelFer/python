import tkinter as tk

def calcular_imc():
    altura = float(altura_entry.get()) / 100
    peso = float(peso_entry.get())
    imc = peso / (altura ** 2)
    imc_label.config(text=f"IMC: {imc:.2f}")

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")

# Cria os widgets
altura_label = tk.Label(janela, text="Altura (cm):")
altura_label.grid(row=0, column=0)

altura_entry = tk.Entry(janela)
altura_entry.grid(row=0, column=1)

peso_label = tk.Label(janela, text="Peso (kg):")
peso_label.grid(row=1, column=0)

peso_entry = tk.Entry(janela)
peso_entry.grid(row=1, column=1)

calcular_button = tk.Button(janela, text="Calcular", command=calcular_imc)
calcular_button.grid(row=2, column=0)

imc_label = tk.Label(janela, text="")
imc_label.grid(row=2, column=1)

# Inicia a janela principal
janela.mainloop()
