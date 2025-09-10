from velha_certo import Velha

jogo = Velha()

while jogo.verificarEspaço ():
 # Desenha o tabuleiro inicial
 jogo.desenharTabuleiro()
 while True:
# Jogada do humano
  jogadaLinha = int(input('Digite a linha: '))
  jogadaColuna = int(input('Digite a coluna: '))
  if jogo.tabuleiro[jogadaLinha][jogadaColuna] == ' ':
     jogo.tabuleiro[jogadaLinha][jogadaColuna] = 'X'
     break
jogo.desenharTabuleiro()

# Jogada da máquina
while True:
   jogadaLinha = jogo.jogarMaquina()
   jogadaColuna = jogo.jogarMaquina()
   if jogo.tabuleiro[jogadaLinha][jogadaColuna] ==' ':
      jogo.tabuleiro[jogadaLinha][jogadaColuna] = 'O'
      print('Máquina jogou')
      break
jogo.desenharTabuleiro()


resultado=jogo.verificarVencedor()

if resultado['X']:
    print('X venceu')
elif resultado['O']:
    print('O venceu')
else:
    print('Empate')