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
)
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
        center=(LARGURA_TELA // 2, 200)
    )

    tela.blit(titulo, rect_titulo)

    # Pontuação
    texto_score = fonte_texto.render(
        f"Pontuação: {pontos}",
        True,
        (255, 255, 255)
    )

    rect_score = texto_score.get_rect(
        center=(LARGURA_TELA // 2, 280)
    )

    tela.blit(texto_score, rect_score)

    # Botões
    reiniciar = fonte_texto.render(
        "[ R ] Reiniciar",
        True,
        (255, 255, 255)
    )

    rect_reiniciar = reiniciar.get_rect(
        center=(LARGURA_TELA // 2, 370)
    )

    tela.blit(reiniciar, rect_reiniciar)

    sair = fonte_texto.render(
        "[ ESC ] Sair",
        True,
        (255, 255, 255)
    )

    rect_sair = sair.get_rect(
        center=(LARGURA_TELA // 2, 430)
    )

    tela.blit(sair, rect_sair)

    pygame.display.flip()

def verificar_colisao_proprio_corpo(cobrinha):
    """Verifica se a cabeça da cobra encostou em alguma parte do corpo."""
    cabeca = cobrinha[0]
    corpo = cobrinha[1:]

    return cabeca in corpo

def sera_fruta_especial():
    return random.choices([True, False], weights=[10, 90], k=1)[0] # há uma chance de 1/10 ou 10% de uma fruta aparecer na tela (peso de True = 10)

def tela_inicial(tela, pontos): #Vou usar de referência para fazer a tela inicial, por enquanto está igual o game over

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
        center=(LARGURA_TELA // 2, 200)
    )

    tela.blit(titulo, rect_titulo)

    # Pontuação
    texto_score = fonte_texto.render(
        f"Pontuação: {pontos}",
        True,
        (255, 255, 255)
    )

    rect_score = texto_score.get_rect(
        center=(LARGURA_TELA // 2, 280)
    )

    tela.blit(texto_score, rect_score)

    # Botões
    reiniciar = fonte_texto.render(
        "[ R ] Reiniciar",
        True,
        (255, 255, 255)
    )

    rect_reiniciar = reiniciar.get_rect(
        center=(LARGURA_TELA // 2, 370)
    )

    tela.blit(reiniciar, rect_reiniciar)

    sair = fonte_texto.render(
        "[ ESC ] Sair",
        True,
        (255, 255, 255)
    )

    rect_sair = sair.get_rect(
        center=(LARGURA_TELA // 2, 430)
    )

    tela.blit(sair, rect_sair)

    pygame.display.flip()

