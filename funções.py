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

# Função para salvar as marcações em um arquivo
def salvarMarcacoes(arquivo, marcacoes):
    with open(arquivo, "w") as f:
        for marcacao in marcacoes:
            nome = marcacao["nome"]
            posicao = marcacao["posicao"]
            linha = f"{nome},{posicao[0]},{posicao[1]}\n"
            f.write(linha)

def carregarMarcacoes(arquivo):
    marcacoes = []
    with open(arquivo, "r") as f:
        for linha in f:
            nome, x, y = linha.strip().split(",")
            posicao = (int(x), int(y))
            marcacao = {"nome": nome, "posicao": posicao}
            marcacoes.append(marcacao)
    return marcacoes

def excluirMarcacoes(arquivo):
    with open(arquivo, "w") as f:
        pass
    