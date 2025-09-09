import random

class Velha():
    def __init__(self):
        self.minhalista = [' ' for _ in range(9)]

    def desenho(self):
        print(' ' + self.minhalista[0] + ' | ' + self.minhalista[1] + ' | ' + self.minhalista[2])
        print('-----------')
        print(' ' + self.minhalista[3] + ' | ' + self.minhalista[4] + ' | ' + self.minhalista[5])
        print('-----------')
        print(' ' + self.minhalista[6] + ' | ' + self.minhalista[7] + ' | ' + self.minhalista[8])

    def vitoria(self):
        combinacoes = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for c in combinacoes:
            if self.minhalista[c[0]] == self.minhalista[c[1]] == self.minhalista[c[2]] != ' ':
                vencedor = self.minhalista[c[0]]
                print(f"\nVitória de {vencedor}!")
                return True
        return False

