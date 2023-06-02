import pygame
from tkinter import Tk
from funções import solicitarNomeEstrela, calcularDistancia, salvarMarcacoes, carregarMarcacoes, excluirMarcacoes

def escrverTexto(texto,cor,x,y,tamanhaFonte):
    fonte = pygame.font.Font(None,tamanhaFonte)
    textoRenderizado = fonte.render(texto, True, cor)
    tela.blit(textoRenderizado, (x, y))

pygame.init()

#cores
branco = (255,255,255)
vermelho = (255,0,0)
amarelo = (255,255,0)

#definir tamanho da tela
tamanho = (1000,550)
tela = pygame.display.set_mode(tamanho)

#fonte
fonte = pygame.font.Font(None,20)

#fps
fps = 60

#marcações das estrelas
marcacoes = []

#linhas entre as estrelas
linhas = []

#carregamento de arquivos
pygame.display.set_caption('Space Marker')
fundo = pygame.image.load('bg.jpg')
icone = pygame.image.load('space.png')
pygame.display.set_icon(icone)

#pasta das marcações
arquivoMarcacoes = 'marcacoes.txt'

#verifica se á arquivos na pasta 
if pygame.key.get_pressed()[pygame.K_x]:
    if arquivoMarcacoes:
        marcacoes = carregarMarcacoes(arquivoMarcacoes)
    else:
        marcacoes = []
else:
    marcacoes = []

#som ambiente
pygame.mixer.music.load("SpaceAudio.mp3")
pygame.mixer.music.play(-1)

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
                    marcacao = {'nome': nomeEstrela, 'posicao': posicao} #dicionario com nome e posção da estrela
                    marcacoes.append(marcacao)

                    #verifica se tiver apenas 1 marcação não marcar
                    if len(marcacoes) >= 2:
                        posicao1 = marcacoes[-2]['posicao']
                        posicao2 = marcacoes[-1]['posicao']
                        linha = (posicao1, posicao2)
                        linhas.append(linha)

        #teclas para interação com as marcações               
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_z:
                if arquivoMarcacoes:
                    salvarMarcacoes(arquivoMarcacoes, marcacoes)
            elif evento.key == pygame.K_x:
                if arquivoMarcacoes:
                    marcacoes = carregarMarcacoes(arquivoMarcacoes)
                    linhas = []
                    for i in range(len(marcacoes) - 1):
                        posicao1 = marcacoes[i]['posicao']
                        posicao2 = marcacoes[i + 1]['posicao']
                        linha = (posicao1, posicao2)
                        linhas.append(linha)
            elif evento.key == pygame.K_c:
                if arquivoMarcacoes:
                    excluirMarcacoes(arquivoMarcacoes)
                    marcacoes = []
                    linhas = []

    #fundo e indicadores de comandos
    tela.blit(fundo,(0,0))
    escrverTexto('Tecle (z) para salvar as marcações',branco,5,10,20)
    escrverTexto('Tecle (x) para carregar as marcações',branco,5,30,20)
    escrverTexto('Tecle (z) para excluir as marcações',branco,5,50,20)

    #desenha linha entre as marcações
    for linha in linhas:
        posicao1, posicao2 = linha
        pygame.draw.line(tela, branco, posicao1, posicao2, 2)

        #escreve a distancia entre as marcações
        meioXdaLinha = (posicao1[0] + posicao2[0]) // 2
        meioYdaLinha = (posicao1[1] + posicao2[1]) // 2
        distancia = calcularDistancia(posicao1, posicao2)
        textoDistancia = (f"({distancia})")
        textoRenderizado = fonte.render(textoDistancia, True, vermelho)
        tela.blit(textoRenderizado, (meioXdaLinha - textoRenderizado.get_width() // 2, meioYdaLinha - textoRenderizado.get_height() // 2))
    
    #faz as marcações
    for marcacao in marcacoes:
        nome = marcacao['nome']
        posicao = marcacao['posicao']
        pygame.draw.circle(tela, amarelo, posicao, 5) 
        texto = (f"{nome} {posicao}")
        textoRenderizado = fonte.render(texto, True, branco) 
        tela.blit(textoRenderizado, (posicao[0] + 15, posicao[1] - 10))
    
    pygame.display.update()
    pygame.time.Clock().tick(fps)

pygame.quit()
