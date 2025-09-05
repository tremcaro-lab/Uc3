class Praia:
    def __init__(self, nome, distancia_do_centro, numero_de_veranistas, tipo_de_acesso):
        """
        Inicializa um objeto Praia com os atributos especificados.

        Args:
            nome (str): O nome da praia.
            distancia_do_centro (float): A distância da praia ao centro da cidade (em km).
            numero_de_veranistas (int): O número aproximado de veranistas na praia.
            tipo_de_acesso (str): O tipo de acesso à praia (ex: "carro", "caminhada", "barco").
        """
        self.nome = nome
        self.distancia_do_centro = distancia_do_centro
        self.numero_de_veranistas = numero_de_veranistas
        self.tipo_de_acesso = tipo_de_acesso

    def __str__(self):
        """
        Retorna uma representação em string do objeto Praia.
        """
        return (f"Praia(Nome: {self.nome}, "
                f"Distância: {self.distancia_do_centro} km, "
                f"Veranistas: {self.numero_de_veranistas}, "
                f"Acesso: {self.tipo_de_acesso})")
praia1 = Praia('Praia do sol', 12.5,300,'carro')
print(praia1)

qtdd_praias=0
qtdd_praias=int(input('informe a qantidade de praias'))
lista_de_praias=[]
for i in range(qtdd_praias):
    nome_praia = input('informe o nome da praia?')
    distancia_centro = int(input('informe a distância da praia do centro'))
    media_veranistas = int(input('informe a média de veranistas'))
    tipo_de_acesso = int(input('informe o tipo de aesso["0"-não afalstado e "1"- afalstado]'))
    
    praia = Praia(nome_praia,distancia_centro,media_veranistas,tipo_de_acesso)
    lista_de_praias.append (praia)
numero_praias_mais_15km=0
for praia in lista_de_praias:
    if praia.distancia_do_centro > 15:
        numero_praias_mais_15km += 1
    
print(f"número de prias que distam mais de 15 km do centro:{numero_praias_mais_15km}")
qtdd_media_veranistas_acesso_nasf=0  
soma_de_veranistas=0
qtd_praias = 0
for praia in lista_de_praias:
    if praia.tipo_de_acesso == 0:
        soma_de_veranistas+= praia.numero_de_veranistas
        qtd_praias+=1

qtdd_media_veranistas_acesso_nasf = soma_de_veranistas/ qtd_praias
print(qtdd_media_veranistas_acesso_nasf)
prias_asf_menos_1000_veranistas = {}       
for praia in lista_de_praias:
    if praia.tipo_de_acesso == 1 and praia.numero_de_veranistas < 1000:
        prias_asf_menos_1000_veranistas.append({'nome': praia.nome,'distancia': praia.distancia_do_centro})

    print(prias_asf_menos_1000_veranistas)
