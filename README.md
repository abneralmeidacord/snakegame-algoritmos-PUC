# Nome do Jogo

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

## Integrantes do grupo

- Nome 1: Abner Cordeiro de Almeida
- Nome 2: Larissa Cravo Carvalho Camara Santos
- Nome 3: Letícia Xavier Abreu
- Nome 4: Mayra Luiza Santos da Silva

## Estrutura do projeto

> - `main.py`: inicia o jogo;
>- `src/jogo.py`: contém o loop principal;
> - `src/config.py`: guarda configurações como tamanho da tela e cores;
> - `src/funcoes.py`: contém funções auxiliares;
> - `src/dados.py`: contém funções de leitura e escrita de arquivos.

## Descrição do jogo

Descreva brevemente a ideia principal do jogo.

> Nosso jogo será um snake game, em que o jogador poderá escolher a cor da sua cobra, ver sua pontuação máxima, iniciar o jogo, ou sair do jogo. Já na tela da gameplay, o jogador controlará uma cobra que coleta frutinhas, e cresce junto com a quantidade frutinhas ingeridas. Os desafios da partida são não encostar em si mesmo e nem nas extremidades da tela.

## Objetivo do jogador

Explique o que o jogador precisa fazer para vencer ou avançar no jogo.
> O objetivo é coletar a maior quantidade possível de frutinhas, evitando colisões com as extremidades da área de movimentação ou consigo mesmo.

## Regras do jogo

- Regra 1: O Jogador começa com 3 três blocos de corpo
- Regra 2: O Jogador não deve encostar nas bordas da área de movimentação
- Regra 3: O Jogador não deve encostar em si mesmo
- Regra 4: Cada frutinha vale 10 ponto e adiciona 1 bloco de corpo
- Regra 5: As frutas especiais valem 50 pontos e retira 1 bloco ao corpo (aparecem somente 5 segundos)

## Controles

Informe as teclas ou comandos utilizados no jogo.

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- ESC: Pausar o jogo

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
