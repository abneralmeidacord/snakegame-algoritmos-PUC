import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    TAMANHO_PIXEL,
    CINZA,
    CAMINHO_RECORDE,
    CAMINHO_RANKING,
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
    verificar_colisao_borda,
    tela_game_over,
)
from src.sprites import pegar_sprite
from src.dados import (
    salvar_recorde,
    carregar_recorde,
    salvar_ranking,
    carregar_ranking
)

# TO DO: Criar tel para colocar o nome

NOME = "Nome Temporário 30"

def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()
    

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    rodando = True
    estado = "jogando"

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

    direçao = (TAMANHO_PIXEL, 0)
    proxima_direçao = direçao

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
    ranking = carregar_ranking(CAMINHO_RANKING)

    # Fonte para o desenho da pontuação
    fonte = pygame.font.Font(None,40)
   

    # Loop principal: processa entrada, atualiza estado e renderiza a cena.
    while rodando:

        relogio.tick(FPS)

        if estado == "game_over":
            tela_game_over(tela, pontos)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False

                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:
                        executar_jogo()
                        return

                    elif evento.key == pygame.K_ESCAPE:
                        rodando = False

            continue

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and direçao != (TAMANHO_PIXEL, 0):
                    proxima_direçao = (-TAMANHO_PIXEL, 0)

                elif evento.key == pygame.K_RIGHT and direçao != (-TAMANHO_PIXEL, 0):
                    proxima_direçao = (TAMANHO_PIXEL, 0)

                elif evento.key == pygame.K_UP and direçao != (0, TAMANHO_PIXEL):
                    proxima_direçao = (0, -TAMANHO_PIXEL)

                elif evento.key == pygame.K_DOWN and direçao != (0, -TAMANHO_PIXEL):
                    proxima_direçao = (0, TAMANHO_PIXEL)
            
        agora = pygame.time.get_ticks()
        
        if agora - tempo_ultimo_movimento >= intervalo_movimento:
            tempo_ultimo_movimento = agora
            direçao = proxima_direçao

            # verificação se colidiu com a fruta 
            proxima_posi_cabeça = (cobrinha[0][0] + direçao[0],cobrinha[0][1]+direçao[1])
            rect_prox_cabeça = pygame.Rect(
                proxima_posi_cabeça[0],
                proxima_posi_cabeça[1],
                TAMANHO_PIXEL,
                TAMANHO_PIXEL,
            ) 
            if verificar_colisao(rect_prox_cabeça,fruit["rect"]):
                crescer = True
            else:
                crescer = False

            cobrinha = movimento_cobrinha(cobrinha, direçao,crescer)
            
            # verificação se colidiu com o próprio 
            cabeca = cobrinha[0]
            corpo = cobrinha[1:]

            if cabeca in corpo:
                estado = "game_over"

        cabeca_x, cabeca_y = cobrinha[0]

        rect_cabeca = pygame.Rect(
            cabeca_x,
            cabeca_y,
            TAMANHO_PIXEL,
            TAMANHO_PIXEL,
        )

        # Verificação de colisão com a fruta
        if verificar_colisao(rect_cabeca, fruit["rect"]):
            pontos = calcular_pontos(pontos, 10)

            # A função usa a largura e altura da tela para gerar as coordenadas, portanto não tem necessidade de verificar se essas posições estão dentro da área da tela. 
            # Além disso, a posição aleátoria não deixa óbvio onde a próxima fruta irá aparecer
            x, y = gerar_posicao_aleatoria(LARGURA_TELA, ALTURA_TELA, TAMANHO_PIXEL, TAMANHO_PIXEL)
            fruit["rect"].x = x
            fruit["rect"].y = y

        # Verificação de colisão da cobra com as bordas 
        if verificar_colisao_borda(rect_cabeca):
            estado = "game_over"


        # Regras de fim de jogo, recorde e atualiza ranking
        if jogador_perdeu(vidas):
            estado = "game_over"

        if NOME not in recorde.keys() or pontos > recorde[NOME]:
            recorde[NOME] = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde, NOME, pontos)
            salvar_ranking(CAMINHO_RANKING, ranking, NOME, pontos)

        pygame.display.set_caption(
            f"{TITULO_JOGO} | Pontos: {pontos} | Recorde: {recorde} | Vidas: {vidas}"
        )

        tela.fill(CINZA)

        # Desenhando os elementos na tela passando a imagem e o rect de cada dicionário
        tela.blit(fruit["imagem"], fruit["rect"])

        # Desenha a pontuação na tela
        texto = fonte.render(f"Pontuação: {pontos}",True,(139,0,0))
        retangulo_texto = texto.get_rect()
        retangulo_texto.centerx = LARGURA_TELA//2
        retangulo_texto.y = 20
        tela.blit(texto,retangulo_texto)

        desenho_cobrinha(tela, cobrinha, direçao, sprites_cobrinha, TAMANHO_PIXEL)
        pygame.display.flip()

    pygame.quit()
