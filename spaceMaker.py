import pygame
from tkinter import Tk
from funções import solicitarNomeEstrela

pygame.init()

#cores
branco = (255,255,255)
preto = (0,0,0)

#definir tamanho da tela
tamanho = (1000,550)
tela = pygame.display.set_mode(tamanho)

#marcações das estrelas
marcacoes = []

#linhas entre as estrelas
linhas = []

executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                posicao = pygame.mouse.get_pos()
                nome_estrela = solicitarNomeEstrela(posicao)
                if nome_estrela is not None:
                    marcacao = {"nome": nome_estrela, "posicao": posicao}
                    marcacoes.append(marcacao)

                    #verifica se tiver apenas 1 marcação não marcar
                    if len(marcacoes) >= 2:
                        posicao1 = marcacoes[-2]['posicao']
                        posicao2 = marcacoes[-1]['posicao']
                        linha = (posicao1, posicao2)
                        linhas.append(linha)
    
    tela.fill(preto)

    #desenha linha entre as marcações
    for linha in linhas:
        pygame.draw.line(tela, (255, 255, 255), linha[0], linha[1], 2)

    for marcacao in marcacoes:
        nome = marcacao["nome"] #nome dado a estrela
        posicao = marcacao["posicao"] #posição da estrela
        pygame.draw.circle(tela, (255, 255, 255), posicao, 10) #desenha circulo marcador da estrela
        texto = f"{nome} - Posição: {posicao}"
        fonte = pygame.font.Font(None, 20)
        textoRenderizado = fonte.render(texto, True, (255, 255, 255)) 
        tela.blit(textoRenderizado, (posicao[0] + 15, posicao[1] - 10))

    pygame.display.update()

pygame.quit()
