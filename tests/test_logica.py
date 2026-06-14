from src.funcoes import calcular_pontos, jogador_perdeu, limitar_valor, verificar_colisao_proprio_corpo
from src.cobrinha import movimento_cobrinha

def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    """Nao deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50

def test_movimento_cobrinha_para_direita_sem_crescer():
    """Deve mover a cobrinha para a direita e manter o mesmo tamanho."""
    cobrinha = [
        (200, 200),
        (160, 200),
        (120, 200),
    ]

    direcao = (40, 0)

    resultado = movimento_cobrinha(cobrinha.copy(), direcao, False)

    assert resultado == [
        (240, 200),
        (200, 200),
        (160, 200),
    ]


def test_movimento_cobrinha_para_baixo_sem_crescer():
    """Deve mover a cobrinha para baixo e manter o mesmo tamanho."""
    cobrinha = [
        (200, 200),
        (200, 160),
        (200, 120),
    ]

    direcao = (0, 40)

    resultado = movimento_cobrinha(cobrinha.copy(), direcao, False)

    assert resultado == [
        (200, 240),
        (200, 200),
        (200, 160),
    ]


def test_movimento_cobrinha_crescendo():
    """Deve mover a cobrinha e aumentar o tamanho quando crescer for True."""
    cobrinha = [
        (200, 200),
        (160, 200),
        (120, 200),
    ]

    direcao = (40, 0)

    resultado = movimento_cobrinha(cobrinha.copy(), direcao, True)

    assert resultado == [
        (240, 200),
        (200, 200),
        (160, 200),
        (120, 200),
    ]


def test_colisao_com_proprio_corpo():
    """Deve retornar True quando a cabeça estiver na mesma posição do corpo."""
    cobrinha = [
        (200, 200),
        (160, 200),
        (200, 200),
        (120, 200),
    ]

    assert verificar_colisao_proprio_corpo(cobrinha) is True


def test_sem_colisao_com_proprio_corpo():
    """Deve retornar False quando a cabeça não estiver no corpo."""
    cobrinha = [
        (200, 200),
        (160, 200),
        (120, 200),
        (80, 200),
    ]

    assert verificar_colisao_proprio_corpo(cobrinha) is False