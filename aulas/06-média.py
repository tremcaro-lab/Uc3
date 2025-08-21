nome=input('nome do aluno')
nota1=float(input('insira a nota do aluno'))
nota2=float(input('insira a nota do aluno '))

media=(nota1+ nota2)/2

if media>6.5 and media<10:
    Situação= ('aprovado')
elif media> 0 and media<6.5:
    situação=(' reprovado')
else:
    print('dados incorretos')

print(f"A média é {media}. O aluno está {situação}")


  