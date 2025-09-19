from velha_certo import Velha

jogo = Velha()
# Desenha o tabuleiro inicial
jogo.desenharTabuleiro
while jogo.verificarEspaço():
    while True:
        try:
        # Jogada do humano
            jogadaLinha = int(input('Digite a linha: '))
            jogadaColuna = int(input('Digite a coluna: '))

            if jogo.tabuleiro[jogadaLinha][jogadaColuna] == ' ':
             jogo.tabuleiro[jogadaLinha][jogadaColuna] = 'X'
            break
        except(ValueError,IndexError,):
           print('O número não existe')
    resultado = jogo.verificarVencedor()
    if resultado['X']:
      print('x venceu')
      break  
    if not jogo.verificarEspaço:
        print('jogo empatou')
        break
    jogo.desenharTabuleiro()

    while True:
        # Jogada da máquina
        jogadaLinha = jogo.jogarMaquina()
        jogadaColuna = jogo.jogarMaquina()

        if jogo.tabuleiro[jogadaLinha][jogadaColuna] == ' ':
            jogo.tabuleiro[jogadaLinha][jogadaColuna] = 'O'
            print('Máquina jogou')
        break
    if resultado['O']:
      print('O venceu')
      break  
    if not jogo.verificarEspaço:
        print('jogo empatou')
        break