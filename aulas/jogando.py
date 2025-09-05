from jogo_da_velha import Velha
import random
jogo=Velha()
jogo.desenho()
jogadap= int(input('digite a posição'))

jogo.minhalista[jogadap]='x'
jogadac= random.randint(0,8)
jogo.minhalista[jogadac]='0'
jogo.desenho()

""""
if jogadap==0 and jogadap==3 and jogadap==6:
 print('VItoria!')

if jogadap==1 and jogadap==4 and jogadap==7:
 print('VItoria!')
if jogadap==2 and jogadap==5 and jogadap==8:
 print('VItoria!')
  
if jogadap==0 and jogadap==1 and jogadap==2:
 print('VItoria!')
if jogadap==3 and jogadap==4 and jogadap==5:
 print('VItoria!')
if jogadap==6 and jogadap==7 and jogadap==8:
 print('VItoria!')
 
if jogadap==0 and jogadap==4 and jogadap==8:
 print('VItoria!')
if jogadap==2 and jogadap== 4 and jogadap==6:
 print('VItoria!')



if jogadac==0 and jogadac==3 and jogadac==6:
 print('derrota')
if jogadac==1 and jogadac==4 and jogadac==7:
 print('derrota')
if jogadac==2 and jogadac==5 and jogadac==8:
 print('derrota')
  
if jogadac==0 and jogadac==1 and jogadac==2:
 print('derrota')
if jogadac==3 and jogadac==4 and jogadac==5:
 print('derrota')
if jogadac==6 and jogadac==7 and jogadac==8:
 print('derrota')
 
if jogadac==0 and jogadac==4 and jogadac==8:
 print('derrota')
if jogadac==2 and jogadac== 4 and jogadac==6:
 print('derrota')
 """