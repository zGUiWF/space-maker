from tkinter import Tk, simpledialog

#pedir o nome da estrela
def solicitarNomeEstrela(posicao):
    Tk().withdraw()
    nomeEstrela = simpledialog.askstring("Nome da Estrela", "Digite o nome da estrela:")
    Tk().destroy()
    return nomeEstrela, posicao