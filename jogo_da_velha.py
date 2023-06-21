import random
import tkinter as tk
from tkinter import messagebox

def jogar():
    opcoes = ["Pedra", "Papel", "Tesoura"]
    escolha_usuario = escolha_var.get()

    if escolha_usuario == "":
        messagebox.showwarning("Aviso", "Por favor, escolha uma opção.")
        return

    escolha_usuario -= 1

    escolha_computador = random.randint(0, 2)

    resultado = ""

    if escolha_usuario == escolha_computador:
        resultado = "Empate!"
    elif (escolha_usuario == 0 and escolha_computador == 2) or \
            (escolha_usuario == 1 and escolha_computador == 0) or \
            (escolha_usuario == 2 and escolha_computador == 1):
        resultado = "Você ganhou!"
    else:
        resultado = "Você perdeu!"

    messagebox.showinfo("Resultado", resultado)

# Criando a janela principal
window = tk.Tk()
window.title("Pedra, Papel e Tesoura")

# Criando os widgets
escolha_var = tk.IntVar()

label = tk.Label(window, text="Escolha uma opção:")
label.pack()

radio_pedra = tk.Radiobutton(window, text="Pedra", variable=escolha_var, value=1)
radio_pedra.pack()

radio_papel = tk.Radiobutton(window, text="Papel", variable=escolha_var, value=2)
radio_papel.pack()

radio_tesoura = tk.Radiobutton(window, text="Tesoura", variable=escolha_var, value=3)
radio_tesoura.pack()

botao_jogar = tk.Button(window, text="Jogar", command=jogar)
botao_jogar.pack()

# Iniciando o loop principal
window.mainloop()