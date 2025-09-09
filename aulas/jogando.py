from jogo_da_velha import *
# 🕹️ Execução de uma rodada
jogo = Velha()
jogo.desenho()

# Jogada do jogador
jogadap = int(input('\nDigite a posição (0-8): '))
if jogo.minhalista[jogadap] == ' ':
    jogo.minhalista[jogadap] = 'x'
else:
    print("Posição ocupada! Encerrando rodada.")
    exit()

# Verifica vitória do jogador
if jogo.vitoria():
    jogo.desenho()
    exit()

# Jogada do computador
jogadac = random.randint(0, 8)
while jogo.minhalista[jogadac] != ' ':
    jogadac = random.randint(0, 8)
jogo.minhalista[jogadac] = '0'

# Exibe tabuleiro atualizado
jogo.desenho()

# Verifica vitória do computador
if jogo.vitoria():
    exit()
