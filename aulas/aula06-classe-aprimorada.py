class Cachorro():
    def __init__(self, raca= 'viralata') :
        self.raca = raca
        self.idade= 10
    def __str__(self) :
        print(' eus sou um cachorro')

cachorro=Cachorro('labrador')
cachorro2 =Cachorro('Pastor Alemão')
cachorro3 =Cachorro()
print(cachorro.raca)
print(cachorro3.raca)