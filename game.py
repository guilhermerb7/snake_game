import pygame
import time
import random

# Inicializar o pygame
pygame.init()

# Definir as cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Definir as dimensões da tela
largura = 600
altura = 400
dis = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobrinha')

# Definir o relógio
clock = pygame.time.Clock()

# Definir o tamanho e a velocidade da cobrinha
tamanho_celula = 10
velocidade = 15

# Definir a fonte
fonte_estilo = pygame.font.SysFont("bahnschrift", 25)
fonte_pontuacao = pygame.font.SysFont("comicsansms", 35)

# Função para exibir a pontuação
def sua_pontuacao(pontos):
    valor = fonte_pontuacao.render("Pontuação: " + str(pontos), True, branco)
    dis.blit(valor, [0, 0])

# Função para desenhar a cobrinha
def nossa_cobrinha(tamanho_celula, lista_cobrinha):
    for x in lista_cobrinha:
        pygame.draw.rect(dis, verde, [x[0], x[1], tamanho_celula, tamanho_celula])

# Função para o loop principal do jogo
def jogo():
    game_over = False
    game_close = False

    # Posições iniciais da cobrinha
    x1 = largura / 2
    y1 = altura / 2

    # Mudanças na posição
    x1_mudou = 0
    y1_mudou = 0

    # Corpo da cobrinha
    lista_cobrinha = []
    comprimento_cobrinha = 1

    # Posições da comida
    comida_x = round(random.randrange(0, largura - tamanho_celula) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura - tamanho_celula) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(preto)
            mensagem = fonte_estilo.render("Você perdeu! Pressione Q para Sair ou C para Jogo Novo", True, vermelho)
            dis.blit(mensagem, [largura / 6, altura / 3])
            sua_pontuacao(comprimento_cobrinha - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_mudou = -tamanho_celula
                    y1_mudou = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_mudou = tamanho_celula
                    y1_mudou = 0
                elif evento.key == pygame.K_UP:
                    y1_mudou = -tamanho_celula
                    x1_mudou = 0
                elif evento.key == pygame.K_DOWN:
                    y1_mudou = tamanho_celula
                    x1_mudou = 0

        if x1 >= largura or x1 < 0 or y1 >= altura or y1 < 0:
            game_close = True
        x1 += x1_mudou
        y1 += y1_mudou
        dis.fill(azul)
        pygame.draw.rect(dis, vermelho, [comida_x, comida_y, tamanho_celula, tamanho_celula])
        lista_cobrinha.append([x1, y1])
        if len(lista_cobrinha) > comprimento_cobrinha:
            del lista_cobrinha[0]

        for x in lista_cobrinha[:-1]:
            if x == [x1, y1]:
                game_close = True

        nossa_cobrinha(tamanho_celula, lista_cobrinha)
        sua_pontuacao(comprimento_cobrinha - 1)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_celula) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura - tamanho_celula) / 10.0) * 10.0
            comprimento_cobrinha += 1

        clock.tick(velocidade)

    pygame.quit()
    quit()

# Iniciar o jogo
jogo()
