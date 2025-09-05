class Veiculo():
    def __init__(self):
     print('veiculo criado')
    def Ligar(self):
       print('ligando')
    def Andar(self):
       print('andando')
    def Frenar(self):
       print('frenando')
    def Virar_a_direita(self):
       print('virando a direita')
    def Virar_a_esquerda(self):
       print('virando a esquerda')
    def Ir_para_trás(self):
       print('indo para trás')

class Carro(Veiculo):
   def __init__(self):
      print('carro Alugado')
   def Abrir_a_porta(self):
      print('Abrindo a porta')
   def Fazer_drfit(self):
      print('Drift feito')
   def leventar_as_janelas(self):
      print('Janela levantada')
   def Abaixar_as_janelas(self):
      print('Janela abaixadas')

class Moto(Veiculo):
   def __init__(self):
      print('Moto alugada')
   def empinar(self):
      print('Moto empinada')
class Caminhao(Carro):
   def __init__(self):
      print('caminhão alugado')
   def abrir_bau(self):
      print('baú aberto')
   def fechar_bau(self):
      print('baú fechado')