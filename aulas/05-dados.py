nome=input("insira seu nome")
idade=int(input("insira sua idade"))
sexo=input("insira o sexo (masculino) ou (feminino)")
if sexo.upper =="MASCULINO":
    sexo="M"
elif sexo.upper=="FEMININO" :
    sexo="F"
else:
    sexo= "gêmero não esperado"

if idade >50:
    print(f"{nome} tem {idade} anos e é experiente {sexo}")
else:
   print(f"{nome} tem {idade} anos e está em treinamento {sexo}")