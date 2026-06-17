import random
from src import config

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

def gerar_posicao_aleatoria(largura, altura, largura_sprite, altura_sprite, cobrinha):
    """Gera um x e y (coordenadas) aleátorias."""
    x = random.randint(0, largura-largura_sprite)
    y = random.randint(0, altura-altura_sprite)

    while (x, y) in cobrinha:
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

def verificar_colisao_proprio_corpo(cobrinha):
    """Verifica se a cabeça da cobra encostou em alguma parte do corpo."""
    cabeca = cobrinha[0]
    corpo = cobrinha[1:]

    return cabeca in corpo

