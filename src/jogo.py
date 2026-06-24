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
    diminuir_cobrinha
)

from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    verificar_colisao,
    gerar_posicao_aleatoria,
    verificar_colisao_borda,
    tela_game_over,
    sera_fruta_especial,
    tela_inicial,
    tocar_musica_jogo,
    tocar_musica_tela_inicial
)
from src.sprites import pegar_sprite
from src.dados import (
    salvar_recorde,
    carregar_recorde,
    salvar_ranking,
    carregar_ranking
)
from src.config import(
    CAMINHO_SOM_GAME_OVER,
    CAMINHO_SOM_COMER,
)

def executar_jogo(mostrar_menu=True, nome_jogador=None):
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""

    estado = "jogando"
    pausado = False

    pygame.init()
    pygame.mixer.init()

    # Carrega os efeitos sonoros.
    som_comer = pygame.mixer.Sound(CAMINHO_SOM_COMER)
    som_game_over = pygame.mixer.Sound(CAMINHO_SOM_GAME_OVER)
    som_comer.set_volume(0.5)
    som_game_over.set_volume(0.7)

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    if mostrar_menu:
        nome_jogador = tela_inicial(tela)

        if nome_jogador is None:
            pygame.quit()
            return

    elif nome_jogador is None:
        nome_jogador = "JOGD"

    pygame.mixer.music.stop()
    tocar_musica_jogo()

    relogio = pygame.time.Clock()
    rodando = True

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
    duracao_fruta_especial = 3000
    tamanho_minimo_cobrinha = 5

    fruit_image = pegar_sprite(
        CAMINHO_SPRITES,
        x=250,
        y=800,
        width=TAMANHO_PIXEL,
        height=TAMANHO_PIXEL,
        scale=0.6,
    )

    especial_fruit_image = pegar_sprite(
        CAMINHO_SPRITES,
        x=150,
        y=800,
        width=TAMANHO_PIXEL,
        height=TAMANHO_PIXEL,
        scale=0.6,
    )

    def criar_fruta(tipo="normal"):
        """Cria a fruta atual em uma posição livre da cobrinha."""
        imagem = fruit_image

        if tipo == "especial":
            imagem = especial_fruit_image

        x, y = gerar_posicao_aleatoria(
            LARGURA_TELA,
            ALTURA_TELA,
            TAMANHO_PIXEL,
            cobrinha,
        )

        return {
            "tipo": tipo,
            "imagem": imagem,
            "rect": imagem.get_rect(topleft=(x, y)),
            "criada_em": pygame.time.get_ticks(),
        }

    fruta_atual = criar_fruta("normal")

    pontos = 0
    vidas = 1
    recorde = carregar_recorde(CAMINHO_RECORDE)
    ranking = carregar_ranking(CAMINHO_RANKING)

    if nome_jogador not in recorde:
        recorde[nome_jogador] = 0

    fonte = pygame.font.Font(None, 40)
    fonte_info = pygame.font.Font(None, 30)

    while rodando:
        relogio.tick(FPS)

        if estado == "game_over":
            tela_game_over(tela, pontos)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False

                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:
                        executar_jogo(False, nome_jogador)
                        return

                    elif evento.key == pygame.K_ESCAPE:
                        rodando = False

            continue

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    pausado = not pausado

                elif evento.key == pygame.K_ESCAPE and pausado:
                    rodando = False

                elif evento.key == pygame.K_LEFT and direçao != (TAMANHO_PIXEL, 0):
                    proxima_direçao = (-TAMANHO_PIXEL, 0)

                elif evento.key == pygame.K_RIGHT and direçao != (-TAMANHO_PIXEL, 0):
                    proxima_direçao = (TAMANHO_PIXEL, 0)

                elif evento.key == pygame.K_UP and direçao != (0, TAMANHO_PIXEL):
                    proxima_direçao = (0, -TAMANHO_PIXEL)

                elif evento.key == pygame.K_DOWN and direçao != (0, -TAMANHO_PIXEL):
                    proxima_direçao = (0, TAMANHO_PIXEL)

        tela.fill(CINZA)

        texto_pause_info = fonte_info.render("Pressione P para pausar", True, (255, 255, 255))
        tela.blit(texto_pause_info, (20, 20))

        if pausado:
            overlay = pygame.Surface((LARGURA_TELA, ALTURA_TELA), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 50))
            tela.blit(overlay, (0, 0))

            fonte_pause = pygame.font.Font(None, 80)
            fonte_opcoes = pygame.font.Font(None, 50)

            texto_pause = fonte_pause.render("PAUSADO", True, (255, 255, 255))
            rect_pause = texto_pause.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2 - 100))
            tela.blit(texto_pause, rect_pause)

            texto_voltar = fonte_opcoes.render("Pressione P para voltar", True, (255, 255, 255))
            rect_voltar = texto_voltar.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2))
            tela.blit(texto_voltar, rect_voltar)

            texto_sair = fonte_opcoes.render("ESC para sair", True, (255, 255, 255))
            rect_sair = texto_sair.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2 + 60))
            tela.blit(texto_sair, rect_sair)

            pygame.display.flip()
            continue

        agora = pygame.time.get_ticks()

        if fruta_atual["tipo"] == "especial":
            tempo_na_tela = agora - fruta_atual["criada_em"]

            if tempo_na_tela >= duracao_fruta_especial:
                fruta_atual = criar_fruta("normal")

        if agora - tempo_ultimo_movimento >= intervalo_movimento:
            tempo_ultimo_movimento = agora
            direçao = proxima_direçao

            proxima_posi_cabeça = (
                cobrinha[0][0] + direçao[0],
                cobrinha[0][1] + direçao[1],
            )

            rect_prox_cabeça = pygame.Rect(
                proxima_posi_cabeça[0],
                proxima_posi_cabeça[1],
                TAMANHO_PIXEL,
                TAMANHO_PIXEL,
            )

            comeu_fruta = verificar_colisao(rect_prox_cabeça, fruta_atual["rect"])
            crescer = comeu_fruta and fruta_atual["tipo"] == "normal"

            cobrinha = movimento_cobrinha(cobrinha, direçao, crescer)

            if comeu_fruta:
                som_comer.play()

                if fruta_atual["tipo"] == "especial":
                    pontos = calcular_pontos(pontos, 50)

                    if len(cobrinha) > tamanho_minimo_cobrinha:
                        cobrinha = diminuir_cobrinha(cobrinha)

                else:
                    pontos = calcular_pontos(pontos, 10)

                tipo_proxima_fruta = "normal"

                if sera_fruta_especial():
                    tipo_proxima_fruta = "especial"

                fruta_atual = criar_fruta(tipo_proxima_fruta)

            cabeca = cobrinha[0]
            corpo = cobrinha[1:]

            rect_cabeca = pygame.Rect(
                cabeca[0],
                cabeca[1],
                TAMANHO_PIXEL,
                TAMANHO_PIXEL,
            )

            if cabeca in corpo or verificar_colisao_borda(rect_cabeca):
                som_game_over.play()
                pygame.mixer.music.stop()
                estado = "game_over"

        if jogador_perdeu(vidas):
            som_game_over.play()
            pygame.mixer.music.stop()
            estado = "game_over"

        if nome_jogador not in recorde or pontos > recorde[nome_jogador]:
            recorde[nome_jogador] = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde, nome_jogador, pontos)
            salvar_ranking(CAMINHO_RANKING, ranking, nome_jogador, pontos)

        pygame.display.set_caption(
            f"{TITULO_JOGO} | Pontos: {pontos} | Recorde: {recorde[nome_jogador]} | Vidas: {vidas}"
        )

        tela.blit(fruta_atual["imagem"], fruta_atual["rect"])

        texto = fonte.render(f"Pontuação: {pontos}", True, (139, 0, 0))
        retangulo_texto = texto.get_rect()
        retangulo_texto.centerx = LARGURA_TELA // 2
        retangulo_texto.y = 20
        tela.blit(texto, retangulo_texto)

        desenho_cobrinha(tela, cobrinha, direçao, sprites_cobrinha, TAMANHO_PIXEL)
        pygame.display.flip()

    pygame.quit()
