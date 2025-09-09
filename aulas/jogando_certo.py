from velha_certo import Velha

jogo = Velha()

# Desenha o tabuleiro inicial
jogo.desenharTabuleiro()

"""
# Jogada do humano
jogadaLinha = int(input('Digite a linha: '))
jogadaColuna = int(input('Digite a coluna: '))
jogo.tabuleiro[jogadaLinha][jogadaColuna] = 'X'
jogo.desenharTabuleiro()

# Jogada da máquina
jogadaLinha = jogo.jogarMaquina()
jogadaColuna = jogo.jogarMaquina()
jogo.tabuleiro[jogadaLinha][jogadaColuna] = 'O'
print('Máquina jogou')
jogo.desenharTabuleiro()
"""

resultado=jogo.verificarVencedor()

if resultado['X']:
    print('X venceu')
elif resultado['O']:
    print('O venceu')
else:
    print('Empate')