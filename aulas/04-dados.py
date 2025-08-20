nome=input("insira seu nome")
idade=int(input("insira sua idade"))

if idade >50:
    print(f"{nome} tem {idade} anos e é experiente")
elif idade<50:
    print(f"{nome} tem {idade} anos e está em treinamento")
else:
    print(f"{nome} tem {idade} anos")