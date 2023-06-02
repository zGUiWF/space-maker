import pygame
from tkinter import Tk, simpledialog
import math

#pedir o nome da estrela
def solicitarNomeEstrela(posicao):
    root = Tk()
    root.withdraw()
    nomeEstrela = simpledialog.askstring("Nome da Estrela", "Digite o nome da estrela:")
    root.destroy()
    if nomeEstrela is not None and nomeEstrela.strip() != "":
        return nomeEstrela
    else:
        return "Desconhecido"

#calcula distancia entre as marcações
def calcularDistancia(posicao1, posicao2):
    x1, y1 = posicao1
    x2, y2 = posicao2
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(distancia, 2)