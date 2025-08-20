nome=input("insira seu nome")
idade=int(input("insira sua idade"))
sexo=input("insira o sexo (masculino) ou (feminino)")
if sexo =="masculino" or "Masculino":
    sexo=="M"
elif sexo=="feminino" or "Feminino":
    sexo=="F"
else:
    "erro"

if idade >50:
    print(f"{nome} tem {idade} anos e é experiente {sexo}")
elif idade<50:
    print(f"{nome} tem {idade} anos e está em treinamento {sexo}")
else:
    print(f"{nome} tem {idade} anos {sexo}")