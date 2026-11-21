"""
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""

import datetime
dados = {}


dados["Nome"] = str(input("Nome: "))
dados["Ano Nascimento"] = int(input("Ano nascimento: "))
dados["Idade"] = datetime.date.today().year - dados["Ano Nascimento"]
dados["CTPS"] = int(input("Carteira de trabalho: (0 se nao tem) "))
if dados["CTPS"] != 0:
  dados["Ano Contratação"] = int(input("Ano de contratação: "))
  dados["Salario"] = float(input("Salário: "))
  dados["Aposentadoria"] = dados["Idade"] + ((dados["Ano Contratação"] + 35) - datetime.date.today().year)
print("=-"*30)
for k, v in dados.items():
  print(f"O {k} tem valor de {v}")
print(dados)
