import random
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
    CAMINHO_MUSICA_TELA_INICIAL,
    CAMINHO_MUSICA_FUNDO
)
from src.dados import carregar_ranking

import src.config as config



def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)

def gerar_posicao_aleatoria(largura_tela, altura_tela, tamanho_pixel, cobrinha):
    """Gera um x e y (coordenadas) aleátorias."""
    # Como a cobrinha se movimenta com base no tamanho_pixel, o grid da fruta deve ter o mesmo comportamento se o spaw dessa não 
    # pode colidir com a cabeça ou corpo da cobra  

    # quantidade de colunas no grid de movimentação 
    coluna = random.randint(0, largura_tela // tamanho_pixel - 1) 
    # quantidade de linhas no grid de movimentação
    linha = random.randint(0, altura_tela // tamanho_pixel - 1) 
    # a posição deve ser multipla de tamanho pixel (cobrinha inicia com a tupla (200, 200) para seu corpo, logo multipla de 40 que é o 
    # tamanho_pixel)
    x = coluna * tamanho_pixel 
    y = linha * tamanho_pixel

    while (x, y) in cobrinha:
        coluna = random.randint(0, largura_tela // tamanho_pixel - 1) 
        linha = random.randint(0, altura_tela // tamanho_pixel - 1) 
        x = coluna * tamanho_pixel 
        y = linha * tamanho_pixel

    return x, y

def verificar_colisao_borda(rect):
    """Verifica se a cabeça da cobra colidiu com uma das bordas da tela."""
    return (
        rect.left < 0 or
        rect.top < 0 or
        rect.right > config.LARGURA_TELA or
        rect.bottom > config.ALTURA_TELA
    )

def tela_game_over(tela, pontos):

    fonte_titulo = pygame.font.Font(None, 75)
    fonte_texto = pygame.font.Font(None, 40)

    # Fundo escurecido
    overlay = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
    overlay.set_alpha(180)
    overlay.fill((0, 0, 0))
    tela.blit(overlay, (0, 0))

    # Caixa central
    caixa = pygame.Rect(150, 120, 500, 380)
    caixa.center = (LARGURA_TELA // 2, ALTURA_TELA // 2)
    pygame.draw.rect(tela, (25, 25, 25), caixa, border_radius=15)
    pygame.draw.rect(tela, (255, 255, 255), caixa, 3, border_radius=15)

    # Título
    titulo = fonte_titulo.render(
        "GAME OVER",
        True,
        (220, 20, 60)
    )

    rect_titulo = titulo.get_rect(
        center=(LARGURA_TELA // 2, 170)
    )

    tela.blit(titulo, rect_titulo)

    # Pontuação
    texto_score = fonte_texto.render(
        f"Pontuação: {pontos}",
        True,
        (255, 255, 255)
    )

    rect_score = texto_score.get_rect(
        center=(LARGURA_TELA // 2, 210)
    )

    tela.blit(texto_score, rect_score)

    # Botões
    reiniciar = fonte_texto.render(
        "[ R ] Reiniciar",
        True,
        (255, 255, 255)
    )

    rect_reiniciar = reiniciar.get_rect(
        center=(LARGURA_TELA // 2, 400)
    )

    tela.blit(reiniciar, rect_reiniciar)

    sair = fonte_texto.render(
        "[ ESC ] Sair",
        True,
        (255, 255, 255)
    )

    rect_sair = sair.get_rect(
        center=(LARGURA_TELA // 2,440)
    )

    tela.blit(sair, rect_sair)
    exibir_ranking(tela, fonte_texto,250)
    pygame.display.flip()

def verificar_colisao_proprio_corpo(cobrinha):
    """Verifica se a cabeça da cobra encostou em alguma parte do corpo."""
    cabeca = cobrinha[0]
    corpo = cobrinha[1:]

    return cabeca in corpo

def sera_fruta_especial():
    return random.choices([True, False], weights=[10, 90], k=1)[0] # há uma chance de 1/10 ou 10% de uma fruta aparecer na tela (peso de True = 10)

def adicionar_caractere_nome(nome_atual, caractere):
    """Adiciona um caractere ao nome, respeitando o limite de 4 caracteres."""
    if len(nome_atual) >= 4:
        return nome_atual

    if caractere.isalnum():
        return nome_atual + caractere.upper()

    return nome_atual


def apagar_caractere_nome(nome_atual):
    """Remove o ultimo caractere do nome digitado."""
    return nome_atual[:-1]


def pode_iniciar_jogo(nome_digitado):
    """Verifica se o jogador pode iniciar o jogo com o nome digitado."""
    return nome_digitado != ""

def tela_inicial(tela):
    tocar_musica_tela_inicial()

    fonte_titulo = pygame.font.Font(None, 75)
    fonte_texto = pygame.font.Font(None, 40)
    fonte_mensagem = pygame.font.Font(None, 28)
    fonte_ranking = pygame.font.Font(None, 30)

    nome_digitado = ""
    mensagem = "Digite seu nome com ate 4 letras/numeros"

    while True:
        tela.fill((0, 0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return None

                elif evento.key == pygame.K_BACKSPACE:
                    nome_digitado = apagar_caractere_nome(nome_digitado)

                elif evento.key == pygame.K_1 or evento.key == pygame.K_KP1:
                    if pode_iniciar_jogo(nome_digitado):
                        return nome_digitado

                    mensagem = "Digite um nome antes de iniciar"

                else:
                    nome_digitado = adicionar_caractere_nome(nome_digitado, evento.unicode)
                    mensagem = "Digite seu nome com ate 4 letras/numeros"

        # Fundo escurecido
        overlay = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        tela.blit(overlay, (0, 0))

        # Caixa central
        caixa = pygame.Rect(0, 0, 620, 520)
        caixa.center = (LARGURA_TELA // 2, ALTURA_TELA // 2)

        pygame.draw.rect(tela, (25, 25, 25), caixa, border_radius=15)
        pygame.draw.rect(tela, (255, 255, 255), caixa, 3, border_radius=15)

        # Título
        titulo = fonte_titulo.render(
            "COBRINHA.ZIP",
            True,
            (220, 20, 60)
        )

        rect_titulo = titulo.get_rect(
            center=(caixa.centerx, caixa.top + 60)
        )

        tela.blit(titulo, rect_titulo)

        # Mensagem do input
        instrucao = fonte_mensagem.render(
            mensagem,
            True,
            (255, 255, 255)
        )

        rect_instrucao = instrucao.get_rect(
            center=(caixa.centerx, caixa.top + 140)
        )

        tela.blit(instrucao, rect_instrucao)

        # Caixa do nome
        caixa_nome = pygame.Rect(0, 0, 220, 50)
        caixa_nome.center = (caixa.centerx, caixa.top + 195)

        pygame.draw.rect(tela, (255, 255, 255), caixa_nome, border_radius=8)
        pygame.draw.rect(tela, (220, 20, 60), caixa_nome, 3, border_radius=8)

        texto_nome = nome_digitado

        if texto_nome == "":
            texto_nome = "NOME"

        nome_renderizado = fonte_texto.render(
            texto_nome,
            True,
            (25, 25, 25)
        )

        rect_nome = nome_renderizado.get_rect(
            center=caixa_nome.center
        )

        tela.blit(nome_renderizado, rect_nome)

        # Ranking
        exibir_ranking(tela, fonte_ranking, caixa.top + 255)

        # Botão jogar
        jogar = fonte_texto.render(
            "[ 1 ] JOGAR",
            True,
            (255, 255, 255)
        )

        rect_jogar = jogar.get_rect(
            center=(caixa.centerx, caixa.bottom - 85)
        )

        tela.blit(jogar, rect_jogar)

        # Botão sair
        sair = fonte_texto.render(
            "[ ESC ] Sair",
            True,
            (255, 255, 255)
        )

        rect_sair = sair.get_rect(
            center=(caixa.centerx, caixa.bottom - 40)
        )

        tela.blit(sair, rect_sair)

        pygame.display.flip()

        
def exibir_ranking(tela, fonte_texto, y_inicial):
        
        ranking = carregar_ranking(CAMINHO_RANKING)
        ranking_ordenado = sorted(ranking.items(), key=lambda x: x[1], reverse=True)[:5]
    
        titulo_ranking = fonte_texto.render("RANKING", True,(255,255,0))
        rect_titulo_ranking = titulo_ranking.get_rect(center=(LARGURA_TELA//2,y_inicial))
        tela.blit(titulo_ranking,rect_titulo_ranking)
        y = y_inicial+40
        
        for i, (nome,pontos) in enumerate(ranking_ordenado):
            
            if i == 0:
                cor = (255,215,0)
                
            elif i == 1:
                cor = (192,192,192)
            elif i == 2:
                cor = (205,127,50)
            else:
                cor = (255,255,255)
            
            texto = fonte_texto.render(
                    f"{i+1}°- {nome} - {pontos}",True,cor
                )
            rect_texto = texto.get_rect(center=(LARGURA_TELA//2,y)
            )
            tela.blit(texto, rect_texto)
            y+=30
            

        pygame.display.flip()

def tocar_musica_tela_inicial():
    pygame.mixer.music.load(CAMINHO_MUSICA_TELA_INICIAL)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

def tocar_musica_jogo():
    pygame.mixer.music.load(CAMINHO_MUSICA_FUNDO)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)