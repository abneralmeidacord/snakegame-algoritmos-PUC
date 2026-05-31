# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

Escreva aqui o nome provisório do jogo.

> 🔥 COBRINHA.ZIP 😝🤟 

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome 1: Abner Cordeiro de Almeida
- Nome 2: Larissa Cravo Carvalho Camara Santos
- Nome 3: Letícia Xavier Abreu
- Nome 4: Mayra Luiza Santos da Silva

## 3. Tipo de jogo

Indique o tipo de jogo que será desenvolvido.

Exemplos:

- jogo de desviar de obstáculos;
- jogo de coleta de itens;
- labirinto simples;
- jogo de perguntas e respostas;
- jogo de memória;
- Pong;
- Snake;
- Breakout;
- nave desviando de meteoros;
- corrida simples com obstáculos;
- jogo de clique rápido;
- jogo de sobrevivência simples.

Tipo escolhido pelo grupo:

> - Snake;

## 4. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará.

Procure responder:

- O que aparece na tela?
- O que o jogador controla?
- O que o jogador precisa fazer?
- Quais desafios aparecem durante a partida?

Descrição:

> Nosso jogo será um snake game, em que nossa tela inicial o jogador poderá  escolher a cor da sua cobra, ver sua pontuação máxima, iniciar o jogo, ou sair do jogo. Já na tela da gameplay, o jogador controlará uma cobra que se move para cima, baixo, direita e esquerda. Além disso, ela coleta frutinhas, e sua cobra cresce junto com a quantidade frutinhas ingeridas. A tela possui a pontuação no topo e um botão de pause e quando clicado um pop-up o mostra as opções de "Sair do Jogo" ou Continuar". Os desafios da partida são não encostar em si mesmo e nem nas extremidades da tela."

## 5. Objetivo do jogador

Explique qual é o objetivo principal do jogador.

Exemplos:

- coletar o maior número possível de itens;
- sobreviver pelo maior tempo possível;
- chegar até o final do labirinto;
- acertar alvos;
- responder perguntas corretamente;
- evitar obstáculos;
- quebrar todos os blocos.

Objetivo:

> Coletar o maior número de frutinhas, sobreviver o maior tempo possível e não morrer.

## 6. Regras principais

Liste as principais regras do jogo.

Exemplo:

- O jogador começa com 3 vidas.
- Cada moeda coletada vale 10 pontos.
- Cada colisão com obstáculo remove 1 vida.
- A partida termina quando as vidas chegam a zero.
- O jogador vence se alcançar 100 pontos.

Regras do grupo:

- Regra 1: O Jogador começa com 3 três blocos de corpo
- Regra 2: O Jogador não deve encostar nas bordas da área de movimentação
- Regra 3: O Jogador não deve encostar em si mesmo
- Regra 4: Cada frutinha vale 10 ponto e adiciona 1 bloco de corpo
- Regra 5: As frutas especiais valem 50 pontos e retira 1 bloco ao corpo (aparecem somente 5 segundos)

## 7. Condição de vitória

Explique como o jogador vence ou conclui o jogo.

Exemplos:

- atingir determinada pontuação;
- chegar ao final da fase;
- sobreviver até o tempo acabar;
- responder uma quantidade mínima de perguntas;
- quebrar todos os blocos.

Condição de vitória:

> O jogador, não tem uma condição de vitória, mas ele pode superar sua própria pontuação atingindo um novo Highscore.

## 8. Condição de derrota ou encerramento

Explique como o jogador perde ou quando a partida termina.

Exemplos:

- perder todas as vidas;
- acabar o tempo;
- colidir com determinado obstáculo;
- errar muitas perguntas;
- deixar a bola cair, no caso de Breakout ou Pong.

Condição de derrota ou encerramento:

> Colidir com a extremidade da área de movimentação ou colidir com o próprio corpo.

## 9. Elementos previstos no jogo

Descreva os principais elementos que farão parte do jogo.

## Jogador ou elemento principal

Exemplo:

> Um personagem controlado pelas setas do teclado.

Descrição:

> Uma cobra controlada pelas setas do teclado.

## Obstáculos, inimigos ou desafios

Exemplo:

> Obstáculos aparecem em posições aleatórias e devem ser evitados.

Descrição:

> Os blocos de corpo devem ser evitados assim como as extremidades da área de movimentação

## Itens, alvos ou objetos de interação

Exemplo:

> Moedas aparecem na tela e aumentam a pontuação quando coletadas.

Descrição:

> As frutinhas aparecem na tela e aumentam a pontuação e adicionam um bloco do corpo

## Pontuação, vidas, tempo ou progresso

Exemplo:

> O jogador começa com 3 vidas e ganha 10 pontos por item coletado.

Descrição:

> Escreva aqui.

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

Exemplo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- Espaço: realizar ação
- ESC: sair do jogo

Controles do grupo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- ESC: Pausar o jogo

## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Exemplo:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.

Organização planejada:

> - `main.py`: inicia o jogo;
>- `src/jogo.py`: contém o loop principal;
> - `src/config.py`: guarda configurações como tamanho da tela e cores;
> - `src/funcoes.py`: contém funções auxiliares;
> - `src/dados.py`: contém funções de leitura e escrita de arquivos.


## 12. Recursos externos previstos

Informe se o grupo pretende utilizar imagens, sons, fontes, tutoriais ou códigos externos.

Exemplo:

- imagens obtidas de banco gratuito;
- sons gratuitos;
- tutorial usado apenas como referência;
- fonte personalizada.

Recursos previstos:

> - Imagens de frutinha
> - Efeitos sonoros (New Highscore, derrota, e coletando frutinha)

## 13. Principais dificuldades esperadas

Liste as dificuldades que o grupo acredita que poderá enfrentar.

Exemplos:

- movimentação do jogador;
- colisão entre objetos;
- controle de tempo;
- criação do ranking;
- organização do código;
- uso do GitHub;
- testes;
- exibição de textos na tela.

Dificuldades previstas:

- Dificuldade 1: movimentação do jogador;
- Dificuldade 2: colisão entre objetos;
- Dificuldade 3: criação do ranking;
- Dificuldade 4: guardar pontuações por user_name
- Dificuldade 5: versionamento no github
- Dificuldade 6: incluir efeitos sonoros
- Dificuldade 7: divisão de tarefas

## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Esta seção é importante para evitar que o grupo escolha uma ideia grande demais.

Exemplo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, obstáculos aparecendo na tela, sistema de vidas, sistema de pontuação e tela de fim de jogo.

Escopo mínimo:

> Uma cobrinha se controlada pelas setas do teclado, com frutas que aparecem na tela e somam pontuação e a mostram ao fim da partida.

## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Exemplos:

- tela inicial;
- sons;
- fases;
- aumento de dificuldade;
- ranking;
- animações;
- novos tipos de obstáculos;
- diferentes personagens;
- menu de pausa.

Melhorias possíveis:

- Melhoria 1: Loop de Animação da cobrinha
- Melhoria 2: Personalizações do jogo
- Melhoria 3: Mapas diferentes
- Melhoria 4: Multiplayer Local duas cobras uma controlada pelas setas (Player1) e a outra pelo WASD (player2)