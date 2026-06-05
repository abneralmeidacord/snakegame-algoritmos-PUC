import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    TAMANHO_PIXEL,
    CINZA,
    CAMINHO_RECORDE,
    CAMINHO_SPRITES,
)

from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    verificar_colisao,
    tomar_dano,
    gerar_posicao_aleatoria,
)
from src.sprites import pegar_sprite
from src.dados import (
    salvar_recorde,
    carregar_recorde,
)


def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()
    

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    rodando = True

    # 1. Carregando as imagens recortadas do Spritesheet


    # Jogador: usando tamanho 110x110 para capturar o quadrado perfeitamente
    player_image = pegar_sprite(CAMINHO_SPRITES, x=110, y=120, width=190, height=190, scale=0.5)

    # Fruta
    fruit_image = pegar_sprite(CAMINHO_SPRITES, x=500, y=830, width=TAMANHO_PIXEL, height=TAMANHO_PIXEL, scale=0.5)

    # Morcego: usando tamanho 180x120 por causa das asas abertas
    bat_image    = pegar_sprite(CAMINHO_SPRITES, x=905, y=1060, width=200, height=130, scale=0.5)
    
    # 2. Criando a estrutura de Sprites usando Dicionários
    jogador = {
        "imagem": player_image,
        "rect": player_image.get_rect(topleft=(100, 100))
    }

    #Tirei a inicialização com posição fixa -> Antes: primeira fruta iniciava em uma posição fixa / Agora: Começa em uma posição aleatória
    #Também podemos tirar para deixar uma cor única (sem imagem/sprite)
    fruit = {
        "imagem": fruit_image, 
        "rect": fruit_image.get_rect(topleft=gerar_posicao_aleatoria(LARGURA_TELA, ALTURA_TELA, TAMANHO_PIXEL, TAMANHO_PIXEL)) 
    }
    
    inimigo = {
        "imagem": bat_image,
        "rect": bat_image.get_rect(topleft=(200, 500))
    }

    velocidade = 5
    pontos = 0
    vidas = 3
    recorde = carregar_recorde(CAMINHO_RECORDE)

    # Loop principal: processa entrada, atualiza estado e renderiza a cena.
    while rodando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        teclas = pygame.key.get_pressed()

        # Movimentação alterando direto os eixos X e Y do retângulo do jogador
        if teclas[pygame.K_LEFT]:
            jogador["rect"].x -= velocidade
        if teclas[pygame.K_RIGHT]:
            jogador["rect"].x += velocidade
        if teclas[pygame.K_UP]:
            jogador["rect"].y -= velocidade
        if teclas[pygame.K_DOWN]:
            jogador["rect"].y += velocidade

        # Limitando o jogador dentro das bordas da tela usando as propriedades do Rect
        jogador["rect"].x = limitar_valor(jogador["rect"].x, 0, LARGURA_TELA - jogador["rect"].width)
        jogador["rect"].y = limitar_valor(jogador["rect"].y, 0, ALTURA_TELA - jogador["rect"].height)

        # Verificação de colisão com a fruta
        if verificar_colisao(jogador["rect"], fruit["rect"]):
            pontos = calcular_pontos(pontos, 10)

            # A função usa a largura e altura da tela para gerar as coordenadas, portanto não tem necessidade de verificar se essas posições estão dentro da área da tela. 
            # Além disso, a posição aleátoria não deixa óbvio onde a próxima fruta irá aparecer
            x, y = gerar_posicao_aleatoria(LARGURA_TELA, ALTURA_TELA, TAMANHO_PIXEL, TAMANHO_PIXEL)
            fruit["rect"].x = x
            fruit["rect"].y = y

        # Verificação de colisão da cobre com as bordas 
        if function.verificar_colisao_borda(pygame.cobra["rect"]):
            rodando = False


        # Verificação de colisão com o Inimigo
        if verificar_colisao(jogador["rect"], inimigo["rect"]):
            vidas = tomar_dano(vidas, 1)

            # Afasta o inimigo ao colidir
            inimigo["rect"].x += 80
            inimigo["rect"].y += 50

            if inimigo["rect"].x > LARGURA_TELA - inimigo["rect"].width:
                inimigo["rect"].x = 50
            if inimigo["rect"].y > ALTURA_TELA - inimigo["rect"].height:
                inimigo["rect"].y = 50

        # Regras de fim de jogo e recorde
        if jogador_perdeu(vidas):
            rodando = False

        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)

        pygame.display.set_caption(
            f"{TITULO_JOGO} | Pontos: {pontos} | Recorde: {recorde} | Vidas: {vidas}"
        )

        tela.fill(CINZA)

        # Desenhando os elementos na tela passando a imagem e o rect de cada dicionário
        tela.blit(fruit["imagem"], fruit["rect"])
        tela.blit(inimigo["imagem"], inimigo["rect"])
        tela.blit(jogador["imagem"], jogador["rect"])

        pygame.display.flip()

    pygame.quit()