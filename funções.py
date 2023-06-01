import pygame
from tkinter import Tk, simpledialog

#definir tamanho da tela
tamanho = (1000, 550)
tela = pygame.display.set_mode(tamanho)

#pedir o nome da estrela
def solicitarNomeEstrela(posicao):
    root = Tk()
    root.withdraw()
    nome_estrela = simpledialog.askstring("Nome da Estrela", "Digite o nome da estrela:")
    root.destroy()
    if nome_estrela is not None and nome_estrela.strip() != "":
        return nome_estrela
    else:
        return "Desconhecido"
