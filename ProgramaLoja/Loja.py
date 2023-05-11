import tkinter as tk
import pandas as pd
import sqlite3

#criação de interface
root = tk.Tk()
root.title("Gerenciador de estoque e finanças")

#criar widgets para add/editar produtos
nome_label = tk.Label(root, text="Nome:")
nome_label.grid(row=0, column=0)
nome_entry = tk.Entry(root)
nome_entry.grid(row=0, column=1)

quantidade_label = tk.Label(root, text="Quantidade:")
quantidade_label.grid(row=1, column=0)
quantidade_entry = tk.Entry(root)
quantidade_entry.grid(row=1, column=1)

preco_label = tk.Label(root, text="Preço:")
preco_label.grid(row=2, column=0)
preco_entry = tk.Entry(root)
preco_entry.grid(row=2, column=1)

#adicionar um botão
adicionar_button = tk.Button(root, text="Adicionar")
adicionar_button.grid(row=3, column=1)

#criar tabela para exibir estoque
estoque_label = tk.Label(root, text="Estoque")
estoque_label.grid(row=4, column=0, columnspan=2)

tabela_estoque = tk.Frame(root)
tabela_estoque.grid(row=5, column=0, columnspan=2)

#criar widgets para visualizar e exporta relatorio financeiro
relatorios_label = tk.Label(root, text="Relatorio Financeiro")
relatorios_label.grid(row=6, column=0, columnspan=2)

vendas_label = tk.Label(root, text="Vendas totais:")
vendas_label.grid(row=7, column=0)
vendas_entry = tk.Entry(root)
vendas_entry.grid(row=7, column=1)

lucro_label = tk.Label(root, text="Lucro:")
lucro_label.grid(row=8, column=0)
lucro_entry = tk.Entry(root)
lucro_entry.grid(row=8, column=1)

exportar_button = tk.Button(root, text="Exportar para csv")
exportar_button.grid(row=9, column=0, columnspan=2)

def adicionar_produto():
    # obter dados do produto a partir dos campos de entrada
    nome = nome_entry.get()
    quantidade = quantidade_entry.get()
    preco = preco_entry.get()
    
    # adicionar produto ao dateframe do estoque
    novo_produto = pd.DataFrame({"Nome": [nome], "Quantidade": [quantidade], "Preço": [preco]})
    estoque = pd.concat([estoque, novo_produto], ignore_index=True)

    #atualizar tabela do estoque
    for widget in tabela_estoque.winfo_children():
        widget.destroy()
    for i, col in enumerate(estoque.columns):
        label = tk.Label(tabela_estoque, text=col, relief=tk.RIDGE, width=20)
        label.grid(row=0, column=i)
    for i, row in estoque.iterrows():
        for j, val in enumerate(row):
            label = tk.Label(tabela_estoque, text=val, relief=tk.RIDGE, width=20)
            label.grid(row=i+1, column=j)

def salvar_esqtoque():
    # conectar ao banca de dado
    conn = sqlite3.connect("estoque.db")
    c = conn.cursor

    # criar tabela se ela não exsite
    c.execute('''CREATE TABLE IF NOT EXISTS estoque
                 (nome text, quantidade integer, preco real)''')
    
     # inserir dados do estoque na tabela
    for i, row in estoque.iterrows():
        c.execute(f"INSERT INTO estoque VALUES ('{row['Nome']}', {row['Quantidade']}, {row['Preço']})")
        
    # confirmar mudanças e fechar conexão com banco de dados
    conn.commit()
    conn.close()

# DaraFrame para armazenar o estoque
estoque = pd.DataFrame(columns=["Nome", "Quantidade", "Preço"])

root.mainloop()