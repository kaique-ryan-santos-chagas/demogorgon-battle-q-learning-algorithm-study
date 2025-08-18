import random 
import numpy as np
import os
import time

# Parâmetros do Q-Learning

alpha = 0.1     # taxa de aprendizado 
gamma = 0.9     # fator de desconto
epsilon = 0.1   # taxa de exploração
d20 = 20       # dado de 20 lados

# Estados e ações

states = [(hooper_life, demo_life) for hooper_life in range(0, 110, 10) for demo_life in range(0, 110, 10)]
actions = ['ataque', 'cura', 'esquivar'] 
q_table = {}

# Inicializando a Q-table

for state in states:
    q_table[state] = {action: 0.0 for action in actions}

def choose_action(state):
    if random.uniform(0, 1) < epsilon:
        return random.choice(actions)
    return max(q_table[state], key=q_table[state].get)


def take_action(player_action, agent_action, hopper_hp, demo_hp): 

    print('Rolando d20 do Hopper...')
    rol_hopper = random.randint(1, d20) 
    print(f'Resultado: {rol_hopper}')
    print('Rolando d20 do Demogorgon...')
    rol_demo = random.randint(1, d20) 
    print(f'Resultado: {rol_demo}')

    if player_action == 'ataque' and agent_action != 'esquivar' and rol_hopper > 10:
        demo_hp -= 20
    if player_action == 'cura' and rol_hopper > 10:
        hopper_hp = min(hopper_hp + 10, 100)
    if player_action == 'esquivar' and agent_action == 'ataque' and rol_hopper > 10:
        pass
    elif player_action == 'esquivar' and agent_action == 'ataque' and rol_hopper < 10:
        hopper_hp -= 20

    if agent_action == 'ataque' and player_action != 'esquivar' and rol_demo > 10:
        hopper_hp -= 20
    if agent_action == 'cura' and rol_demo > 10:
        demo_hp = min(demo_hp + 10, 100)
    if agent_action == 'esquivar' and player_action == 'ataque' and rol_demo > 10:
        pass
    elif agent_action == 'esquivar' and player_action == 'ataque' and rol_demo < 10:
        demo_hp -= 20
    
    hopper_hp = max(hopper_hp, 0)
    demo_hp = max(demo_hp, 0)

    return hopper_hp, demo_hp


def get_reward(hopper_hp, demo_hp, done): 
    if done:
        if hopper_hp <= 0:
            return 100
        elif demo_hp <= 0:
            return -100
    else:
        if hopper_hp > demo_hp:
            return -10
        elif hopper_hp < demo_hp:
            return 10
        else:
            return 0


# ---------- FASE DE TREINAMENTO ----------

print("Treinando Demogorgon...")
episodes = 1000

for _ in range(episodes):
    hopper_hp = 100
    demo_hp = 100 
    done = False

    while not done:
        state = (hopper_hp, demo_hp)
        agent_action = choose_action(state)
        player_action = random.choice(actions)  # simula jogador aleatório

        new_hopper_hp, new_demo_hp = take_action(player_action, agent_action, hopper_hp, demo_hp)

        reward = get_reward(new_hopper_hp, new_demo_hp, new_hopper_hp == 0 or new_demo_hp == 0)
        new_state = (new_hopper_hp, new_demo_hp)

        old_value = q_table[state][agent_action]
        future_max = max(q_table[new_state].values())

        q_table[state][agent_action] = old_value + alpha * (reward + gamma * future_max - old_value)

        hopper_hp, demo_hp = new_hopper_hp, new_demo_hp
        done = hopper_hp == 0 or demo_hp == 0

print("Treinamento completo!\n")


# ---------- JOGO COM O JOGADOR ----------

def play_game():
    
    hopper_hp = 100
    demo_hp = 100
    turn = 1

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"=== BATALHA - Turno {turn} ===")
        print(f"Hopper:     {hopper_hp} HP") 
        print(f"Demogorgon: {demo_hp} HP\n")

        # Turno do jogador
        print("Suas ações:")
        print("1. Atacar")
        print("2. Curar")
        print("3. Esquivar")
        choice = input("Escolha sua ação (1, 2 ou 3): ")
        while choice not in ['1', '2', '3']:
            choice = input("Escolha inválida. Digite 1, 2 ou 3: ")

        if choice == '1':
            player_action = 'ataque'
        elif choice == '2':
            player_action = 'cura'
        elif choice == '3':
            player_action = 'esquivar'

        # Ação do agente (Demogorgon)
        state = (hopper_hp, demo_hp)
        agent_action = max(q_table[state], key=q_table[state].get)

        print(f"\nVocê escolheu: {player_action.upper()}")
        print(f"Demogorgon escolheu: {agent_action.upper()}")
        time.sleep(1)

        hopper_hp, demo_hp = take_action(player_action, agent_action, hopper_hp, demo_hp)

        if hopper_hp <= 0:
            print("\nVocê morreu...")
            break
        elif demo_hp <= 0:
            print("\nVocê matou o Demogorgon! 🧨")
            break

        turn += 1
        time.sleep(1.5)


# Inicia o jogo no terminal
play_game()
