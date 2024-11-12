import tkinter as tk
from tkinter import PhotoImage
import sqlite3

def salvar_dados(nome, cpf, estado):
    connection = sqlite3.connect("dados.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Tabela1 (nome TEXT, cpf TEXT, estado TEXT)")
    cursor.execute("INSERT INTO Tabela1 VALUES (?, ?, ?)", (nome, cpf, estado))
    connection.commit()
    connection.close()
    
def carregar_estados():
    with open("config.txt", "r") as file:
        estados = file.read().split(";")
        estados = [estado.strip() for estado in estados]
    return estados

def VerificarCPF(CPF):
    if len(CPF) != 14 or not CPF[3] == CPF[7] == '.' or CPF[11] != '-':
        return False
    return True

def main():
    root = tk.Tk()
    root.title("Trabalho RAD - y1")

    label_nome = tk.Label(root, text="Nome:")
    label_nome.pack()

    entry_nome = tk.Entry(root)
    entry_nome.pack()

    label_cpf = tk.Label(root, text="CPF:")
    label_cpf.pack()

    entry_cpf = tk.Entry(root)
    entry_cpf.pack()

    label_estado = tk.Label(root, text="Estado:")
    label_estado.pack()

    entry_estado = tk.Entry(root)
    entry_estado.pack()

    # o tal do dropdown
    label_tipo = tk.Label(root, text="Tipo de Trabalho:")
    label_tipo.pack()
    
    tipo_trabalho = tk.StringVar(value="Selecione")
    dropdown_tipo = tk.OptionMenu(root, tipo_trabalho, "CLT", "MEI", "Sócio")
    dropdown_tipo.pack()

    botao_salvar = tk.Button(root, text="Salvar", command=lambda: salvar_dados(entry_nome.get(), entry_cpf.get(), entry_estado.get()))
    botao_salvar.pack()

    root.mainloop()


if __name__ == "__main__":
    main()