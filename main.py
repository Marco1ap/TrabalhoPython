import tkinter as tk
from tkinter import PhotoImage

def main():
    root = tk.Tk()
    root.title("Trabalho RAD - v3")

    # Carregar imagem de fundo
    bg_image = PhotoImage(file="fundo.png")
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Adicionar widgets
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

    botao_salvar = tk.Button(root, text="Salvar", command=lambda: print("Nome:", entry_nome.get(), "CPF:", entry_cpf.get(), "Estado:", entry_estado.get()))
    botao_salvar.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
