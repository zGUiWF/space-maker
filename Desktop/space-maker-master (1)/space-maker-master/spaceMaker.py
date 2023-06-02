import pygame
from tkinter import Tk
from funções import solicitarNomeEstrela, calcularDistancia

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

pygame.display.set_caption("Space Marker")
fundo = pygame.image.load("bg.jpg")
icone = pygame.image.load("space.png")
pygame.display.set_icon(icone)

executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                posicao = pygame.mouse.get_pos()
                nomeEstrela = solicitarNomeEstrela(posicao)
                if nomeEstrela is not None:
                    marcacao = {"nome": nomeEstrela, "posicao": posicao} #dicionario com nome e posção da estrela
                    marcacoes.append(marcacao)

                    #verifica se tiver apenas 1 marcação não marcar
                    if len(marcacoes) >= 2:
                        posicao1 = marcacoes[-2]['posicao']
                        posicao2 = marcacoes[-1]['posicao']
                        linha = (posicao1, posicao2)
                        linhas.append(linha)
    
    tela.blit(fundo,(0,0))


    #desenha linha entre as marcações
    for linha in linhas:
        posicao1, posicao2 = linha
        pygame.draw.line(tela, (255, 255, 255), posicao1, posicao2, 2)

        #escreve a distancia entre as marcações
        meioXdaLinha = (posicao1[0] + posicao2[0]) // 2
        meioYdaLinha = (posicao1[1] + posicao2[1]) // 2
        distancia = calcularDistancia(posicao1, posicao2)
        textoDistancia = (f"({distancia})")
        fonte = pygame.font.Font(None, 20)
        textoRenderizado = fonte.render(textoDistancia, True, (0, 255, 0))
        tela.blit(textoRenderizado, (meioXdaLinha - textoRenderizado.get_width() // 2, meioYdaLinha - textoRenderizado.get_height() // 2))

    for marcacao in marcacoes:
        nome = marcacao["nome"]
        posicao = marcacao["posicao"]
        pygame.draw.circle(tela, (255, 255, 255), posicao, 10) 
        texto = (f"{nome} {posicao}")
        fonte = pygame.font.Font(None, 20)
        textoRenderizado = fonte.render(texto, True, (255, 255, 255)) 
        tela.blit(textoRenderizado, (posicao[0] + 15, posicao[1] - 10))

    pygame.display.update()

pygame.quit()
