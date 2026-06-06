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

from src.cobrinha import (
    sprite_cobrinha,
    movimento_cobrinha,
    desenho_cobrinha,
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

    # 1. Carregando as imagens recortadas do Spritesheet e a cobrinha criada, com o pygame.draw
    
    # Cobrinha
    sprites_cobrinha = sprite_cobrinha(TAMANHO_PIXEL)

    cobrinha = [
        (200, 200),
        (160, 200),
        (120, 200),
        (80, 200),
        (40, 200),  
    ]

    direcao = (TAMANHO_PIXEL, 0)
    proxima_direcao = direcao

    tempo_ultimo_movimento = pygame.time.get_ticks()
    
    intervalo_movimento = 130
    
    # Fruta
    fruit_image = pegar_sprite(CAMINHO_SPRITES, x=500, y=830, width=TAMANHO_PIXEL, height=TAMANHO_PIXEL, scale=0.5)

    
    # 2. Criando a estrutura de Sprites usando Dicionários

    #Tirei a inicialização com posição fixa -> Antes: primeira fruta iniciava em uma posição fixa / Agora: Começa em uma posição aleatória
    
    #Também podemos tirar para deixar uma cor única (sem imagem/sprite)
    fruit = {
        "imagem": fruit_image, 
        "rect": fruit_image.get_rect(topleft=gerar_posicao_aleatoria(LARGURA_TELA, ALTURA_TELA, TAMANHO_PIXEL, TAMANHO_PIXEL)) 
    }

    velocidade = 5
    pontos = 0
    vidas = 1
    recorde = carregar_recorde(CAMINHO_RECORDE)

    # Loop principal: processa entrada, atualiza estado e renderiza a cena.
    while rodando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        teclas = pygame.key.get_pressed()

        # Movimentação alterando direto os eixos X e Y do retângulo do cobrinha
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and direcao != (TAMANHO_PIXEL, 0):
                    proxima_direcao = (-TAMANHO_PIXEL, 0)
                elif evento.key == pygame.K_RIGHT and direcao != (-TAMANHO_PIXEL, 0):
                    proxima_direcao = (TAMANHO_PIXEL, 0)
                elif evento.key == pygame.K_UP and direcao != (0, TAMHO_PIXEL):
                    proxima_direcao = (0, -TAMANHO_PIXEL)
                elif evento.key == pygame.K_DOWN and direcao != (0, -TAMANHO_PIXEL):
                    proxima_direcao = (0, TAMANHO_PIXEL)

        agora = pygame.time.get_ticks()
        
        if agora - tempo_ultimo_movimento >= intervalo_movimento:
            tempo_ultimo_movimento = agora
            direcao = proxima_direcao
            cobra = movimento_cobrinha(cobra, direcao)

        # Limitando o cobrinha dentro das bordas da tela usando as propriedades do Rect
        cobrinha["rect"].x = limitar_valor(cobrinha["rect"].x, 0, LARGURA_TELA - cobrinha["rect"].width)
        cobrinha["rect"].y = limitar_valor(cobrinha["rect"].y, 0, ALTURA_TELA - cobrinha["rect"].height)

        # Verificação de colisão com a fruta
        if verificar_colisao(cobrinha["rect"], fruit["rect"]):
            pontos = calcular_pontos(pontos, 10)

            # A função usa a largura e altura da tela para gerar as coordenadas, portanto não tem necessidade de verificar se essas posições estão dentro da área da tela. 
            # Além disso, a posição aleátoria não deixa óbvio onde a próxima fruta irá aparecer
            x, y = gerar_posicao_aleatoria(LARGURA_TELA, ALTURA_TELA, TAMANHO_PIXEL, TAMANHO_PIXEL)
            fruit["rect"].x = x
            fruit["rect"].y = y


        # Regras de fim de jogo e recorde
        if cobrinha_perdeu(vidas):
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


        desenho_cobrinha(tela, cobrinha, dir, sprites_cobrinha, TAMANHO_PIXEL)
        pygame.display.flip()

    pygame.quit()