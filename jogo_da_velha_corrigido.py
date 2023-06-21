import tkinter as tk
from tkinter import messagebox

class JogoDaVelhaGUI:
    def __init__(self):
        self.jogador_atual = "X"
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        self.janela = tk.Tk()
        self.janela.title("Jogo da Velha")
        self.botoes = [[None for _ in range(3)] for _ in range(3)]

        for linha in range(3):
            for coluna in range(3):
                botao = tk.Button(
                    self.janela,
                    text=" ",
                    font=("Arial", 20, "bold"),
                    width=6,
                    height=3,
                    command=lambda linha=linha, coluna=coluna: self.realizar_jogada(linha, coluna),
                )
                botao.grid(row=linha, column=coluna)
                self.botoes[linha][coluna] = botao

    def reiniciar_jogo(self):
        self.jogador_atual = "X"
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        for linha in range(3):
            for coluna in range(3):
                self.botoes[linha][coluna].configure(text=" ")
                self.botoes[linha][coluna].configure(state=tk.NORMAL)

    def realizar_jogada(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == " ":
            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.botoes[linha][coluna].configure(text=self.jogador_atual, state=tk.DISABLED)

            if self.verificar_vitoria(self.jogador_atual):
                messagebox.showinfo("Fim de jogo", f"O jogador {self.jogador_atual} venceu!")
                self.reiniciar_jogo()
            elif self.verificar_empate():
                messagebox.showinfo("Fim de jogo", "O jogo terminou em empate!")
                self.reiniciar_jogo()
            else:
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

    def verificar_vitoria(self, jogador):
        # Verificar linhas
        for linha in self.tabuleiro:
            if all(celula == jogador for celula in linha):
                return True

        # Verificar colunas
        for coluna in range(3):
            if all(self.tabuleiro[linha][coluna] == jogador for linha in range(3)):
                return True

        # Verificar diagonais
        if (
            self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] == jogador
            or self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] == jogador
        ):
            return True

        return False

    def verificar_empate(self):
        return all(celula != " " for linha in self.tabuleiro for celula in linha)

    def iniciar(self):
        self.janela.mainloop()

# Criar e iniciar o jogo
jogo = JogoDaVelhaGUI()
jogo.iniciar()
