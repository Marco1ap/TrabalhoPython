import tkinter as tk
from tkinter import PhotoImage
import sqlite3
from PIL import Image, ImageTk

def salvar_dados(nome, cpf, estado):
    if not VerificarCPF(cpf):
        print("CPF inválido")
        return
    
    estados = carregar_estados()
    if estado not in estados:
        print("Estado inválido")
        return
 
    connection = sqlite3.connect("dados.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Tabela1 (nome TEXT, cpf TEXT, estado TEXT)")
    cursor.execute("INSERT INTO Tabela1 VALUES (?, ?, ?)", (nome, cpf, estado))
    connection.commit()
    connection.close()
    print("Dados salvos com sucesso.")

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
    root.geometry("400x400")  # Ajuste o tamanho da janela conforme necessário

    # Carregar e redimensionar a imagem de fundo
    imagem_fundo = Image.open("fundo.png")
    imagem_fundo = imagem_fundo.resize((400, 400), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(imagem_fundo)

    # Criar o Canvas e adicionar a imagem de fundo
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    # Adicionar widgets sobre o Canvas
    label_nome = tk.Label(root, text="Nome:", bg="white")  # Defina a cor de fundo para melhorar a visibilidade
    canvas.create_window(200, 50, window=label_nome)

    entry_nome = tk.Entry(root)
    canvas.create_window(200, 80, window=entry_nome)

    label_cpf = tk.Label(root, text="CPF:", bg="white")
    canvas.create_window(200, 110, window=label_cpf)

    entry_cpf = tk.Entry(root)
    canvas.create_window(200, 140, window=entry_cpf)

    label_estado = tk.Label(root, text="Estado:", bg="white")
    canvas.create_window(200, 170, window=label_estado)

    entry_estado = tk.Entry(root)
    canvas.create_window(200, 200, window=entry_estado)

    # Adicionar o dropdown para Tipo de Trabalho
    label_tipo = tk.Label(root, text="Tipo de Trabalho:", bg="white")
    canvas.create_window(200, 230, window=label_tipo)
    
    tipo_trabalho = tk.StringVar(value="Selecione")
    dropdown_tipo = tk.OptionMenu(root, tipo_trabalho, "CLT", "MEI", "Sócio")
    canvas.create_window(200, 260, window=dropdown_tipo)

    botao_salvar = tk.Button(root, text="Salvar", command=lambda: salvar_dados(entry_nome.get(), entry_cpf.get(), entry_estado.get()))
    canvas.create_window(200, 300, window=botao_salvar)

    root.mainloop()

if __name__ == "__main__":
    main()
