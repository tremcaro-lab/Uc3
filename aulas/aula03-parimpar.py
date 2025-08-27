'''
programa para definir se um número é par ou impar
'''
def verificarParimpar(numero):
    if (numero% 2 ==0):
        return 'o número é par'
    else:
        return 'o número é impar'
    
valor= int (input("Digite um número"))

print(verificarParimpar(valor))