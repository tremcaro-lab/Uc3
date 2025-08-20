nome=input('nome do aluno')
nota1=float(input('insira a nota do aluno'))
nota2=float(input('insira a nota do aluno '))

media=(nota1+ nota2)/2

if media>=6.5 and media<10:
    print(f'{media} aprovado')
elif media> 0 and media<6.5:
    print(f'{media} reprovado')
else:
    print('dados incorretos')


  