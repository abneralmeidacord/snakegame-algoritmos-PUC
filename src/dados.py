def salvar_recorde(caminho_arquivo, recordes_atuais, nome_user, pontuacao):
    """Salva a pontuação recorde em arquivo texto."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        #Coloca o header
        arquivo.write("nome,pontucao")
        #Troca a pontuação para o determinado usuário 
        recordes_atuais[nome_user] = pontuacao
        #Salva os recordes no arquivo
        for nome, recorde in recordes_atuais.items():
            arquivo.write(f"\n{nome},{recorde}")

def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo; retorna {} se não existir valor válido."""
    try:
        recordes = {}
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.readlines()
            for i in range(len(conteudo)):
                # Pula primeira linha de "cabeçalho" no arquivo (Apenas para mostrar o que os dados representam)
                if i == 0:
                    continue

                lista_formatada = conteudo[i].strip("\n").split(",")
                
                if len(lista_formatada) >= 2 and lista_formatada[1].isdigit():
                    recordes[lista_formatada[0]] = int(lista_formatada[1]) 
                
            return recordes

    except FileNotFoundError:
        return {}

def salvar_ranking(caminho_arquivo, ranking_atual, nome_user, pontuacao):
    """Salva a pontuação do ranking em arquivo texto."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:

        # Caso o função carregar_ranking volte com {}, o primeiro jogado ficará em primeiro lugar
        # Adiciona o usuário de qualquer modo
        # Se o usuário já existir, a pontuação é sobreposta
        ranking_atual[nome_user] = pontuacao

        # Cria um outro dicionário, mas ordenado via pontuação
        # O lambda funciona como uma função anônima (não tem nome), em que (nesse caso) receberá uma tupla como parametro 
        # chamado item no formato (nome, pontuacao) e retornará o item[1] que corresponde à pontuação, 
        # A chamada dessa função ocorrerá em cada itineração da função sorted
        #O reverse é para ser em ordem decrescente
        lista_ranking_ordenado = sorted(ranking_atual.items(), key=lambda item: item[1], reverse=True)

        # Caso não tenha atingido nenhuma colocação, mas o ranking está incompleto, o user terá colocação
        # pois deve-se recortar os 3 primeiros. OBS.: o sorted retorna uma lista de tuplas, 
        # ent deve-se converter para dicionário. Antes disso deve-se fazer o recorte (slice) na lista, pois dicionários 
        # não são fatiáveis
        ranking_ordenado = dict(lista_ranking_ordenado[:3])
        
        # Coloca cabeçalho para facilitar a identificação dos campos/colunas
        arquivo.write("nome,pontucao")
        # Escreve as linhas no arquivo 
        for nome, pontos in ranking_ordenado.items():
            arquivo.write(f"\n{nome},{pontos}")

def carregar_ranking(caminho_arquivo):
    """Carrega o ranking salvo; retorna {} se não existir valor válido."""
    try:
    
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            #Estrutura que será retornada => {A: pontuacao, B: pontuacao, C: pontuacao}
            ranking = {}
            conteudo = arquivo.readlines()
            # Pula primeira linha de "cabeçalho" no arquivo (Apenas para mostrar o que os dados representam)
            for i in range(1, 4):

                if i >= len(conteudo):
                    continue
                
                lista_formatada = conteudo[i].strip("\n").split(",")

                if len(lista_formatada) >= 2:
                    ranking[lista_formatada[0]] = int(lista_formatada[1])
                
            return ranking

    except FileNotFoundError:
        return {}