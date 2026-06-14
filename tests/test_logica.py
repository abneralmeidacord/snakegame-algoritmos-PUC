from src.funcoes import calcular_pontos, jogador_perdeu, limitar_valor, verificar_colisao_proprio_corpo
from src.cobrinha import movimento_cobrinha
from src.dados import carregar_ranking, salvar_ranking, carregar_recorde, salvar_recorde


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

def test_salvar_e_carregar_recorde(tmp_path):
    """Deve persistir e recuperar corretamente o recorde de um jogador."""
    # o tmp_path é pq é necessário um arquivo para executar as funções. Para quando rodar o teste não ficar criando usuários imaginários para testar as 
    # funções, o pytest tem esse recurso que cria uma pasta temporária exclusiva para cada teste. Assim os arquivos ficam isolados e são limpos automaticamente pelo pytest 
    # quando rodar os testes novamente


    caminho = tmp_path / "recorde.txt"
    salvar_recorde(str(caminho), {}, "joao", 100)
    recorde = carregar_recorde(str(caminho))
    assert recorde["joao"] == 100


def test_carregar_recorde_arquivo_inexistente(tmp_path):
    """Deve retornar dicionario vazio quando o arquivo de recorde nao existe."""
    caminho = tmp_path / "inexistente.txt"
    assert carregar_recorde(str(caminho)) == {}


def test_salvar_ranking_mantem_apenas_top_3(tmp_path):
    """Deve manter somente os 3 melhores jogadores no ranking apos salvar."""
    caminho = tmp_path / "ranking.txt"
    ranking_inicial = {"ana": 300, "bob": 200, "carol": 150, "davi": 50}
    salvar_ranking(str(caminho), ranking_inicial, "novo", 10)
    ranking = carregar_ranking(str(caminho))
    assert len(ranking) == 3
    assert ranking == {"ana": 300, "bob": 200, "carol": 150}


def test_salvar_ranking_atualiza_pontuacao_existente(tmp_path):
    """Deve sobrescrever a pontuacao quando o jogador ja existe no ranking."""
    caminho = tmp_path / "ranking.txt"
    salvar_ranking(str(caminho), {"alice": 50}, "alice", 999)
    ranking = carregar_ranking(str(caminho))
    assert ranking["alice"] == 999


def test_carregar_ranking_arquivo_inexistente(tmp_path):
    """Deve retornar dicionario vazio quando o arquivo de ranking nao existe."""
    caminho = tmp_path / "inexistente.txt"
    assert carregar_ranking(str(caminho)) == {}


def test_ranking_ordenado_por_pontuacao(tmp_path):
    """Deve retornar os jogadores em ordem decrescente de pontuacao."""
    caminho = tmp_path / "ranking.txt"
    ranking_inicial = {"carlos": 80, "beatriz": 500, "antonio": 200}
    salvar_ranking(str(caminho), ranking_inicial, "beatriz", 500)
    ranking = carregar_ranking(str(caminho))
    pontuacoes = list(ranking.values())
    assert pontuacoes == sorted(pontuacoes, reverse=True)


def test_ranking_cheio_substitui_mais_fraco_por_pontuacao_maior(tmp_path):
    """Deve substituir o mais fraco quando um novo jogador entra com pontuacao maior."""
    caminho = tmp_path / "ranking.txt"
    ranking_inicial = {"ana": 300, "bob": 200, "carol": 100}
    salvar_ranking(str(caminho), ranking_inicial, "davi", 150)
    ranking = carregar_ranking(str(caminho))
    assert len(ranking) == 3
    assert ranking == {"ana": 300, "bob": 200, "davi": 150}