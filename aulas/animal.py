class Animal():
    def __init__(self) :
        print('Animal Criado !')
    def quemSouEu(self):
        print('eu sou um animal')
    def comer(self):
        print('Comendo...')
class Cachorro(Animal):
    def quemSouEu(self):
        print('Eu sou um cachorro')
class Jacare(Animal):
    def nadar(self):
        print('nadando')

animal= Animal()
animal.quemSouEu()
cachorro= Cachorro()
cachorro.quemSouEu()
jacare= Jacare()
jacare.nadar()
