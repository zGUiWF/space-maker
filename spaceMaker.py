import pygame
from tkinter import Tk
from funções import solicitarNomeEstrela

pygame.init()

#cores
branco = (255,255,255)

#obter tamanho da tela
largura, altura = pygame.display.Info().current_w, pygame.display.Info().current_h

#definir tamanho da tela
tela = pygame.display.set_mode((largura, altura), pygame.FULLSCREEN)

executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                #posição do mouse após o click
                posicao = pygame.mouse.get_pos()
                nomeEstrela, posicao = solicitarNomeEstrela(posicao)

    pygame.display.update()

pygame.quit()
