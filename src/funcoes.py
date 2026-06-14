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

def gerar_posicao_aleatoria(largura, altura, largura_sprite, altura_sprite):
    """Gera um x e y (coordenadas) aleátorias."""
    x = random.randint(0, largura-largura_sprite)
    y = random.randint(0, altura-altura_sprite)

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