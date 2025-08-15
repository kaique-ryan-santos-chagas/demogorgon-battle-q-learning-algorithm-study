# <p align="center">Stranger Things - Demogorgon Battle</p>

## Conceito

Este projeto consiste em uma prova de conceito da aplicação de algoritmos de Aprendizado por Reforço (área pertencente a Inteligência Artificial) em jogos digitais. O intuito é provar que o treinamento de agentes inteligentes pode ser um divisor de águas na forma como inimigos e NPCs se comportam nas interações com os jogadores e com o ambiente. 
Nesse estudo foi aplicado o algoritmo Q-Learning que se comporta de forma perfeita com a implementação em jogos digitais, por tratar o agente como NPC e o próprio ambiente do jogo se torna o ambiente de aprendizado do agente. 

## O Jogo

O jogo implementado nesse projeto é um simples software de terminal, podendo ser executado em qualquer SO. O jogo consiste em uma batalha fictícia entre o personagem Hopper e o monstro Demogorgon inspirados na série Stranger Things. A batalha é estruturada em turnos e possuí ações como Ataque, Cura e Esquiva, tanto para o jogador, quanto para o agente. Vence quem matar o outro primeiro. 

## Estrutura de aprendizado do agente 

O agente aprende através dos estados e ações. Os estados consistem basicamente no HP do jogador e no HP do agente, no caso, a quantidade de vida do Hopper e a quantidade de vida do Demogorgon. Esses estados vão influenciar nas recompensas o punições que agente sofrerá durante o jogo. As ações tanto para o jogador, quanto para o agente são Ataque, Cura e Esquiva. 

## Desafios 

O grande desafio é equilibrar o jogo a ponto da IA não quebrar o sistema de combate se tornando invencível para o jogador... O grande ponto chave do algoritmo de Q-Learning é quando a máquina encontra a política perfeita para vencer o desafio imposto para ela, nisso a IA acaba achando a estratégia perfeita para derrotar o jogador após o treinamento do agente. 

<img src="https://github.com/user-attachments/assets/c9a5d343-9c89-4a1b-986c-aa5ea2fdaa78" />
