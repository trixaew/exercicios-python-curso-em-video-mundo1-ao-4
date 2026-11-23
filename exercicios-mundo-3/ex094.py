"""
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
"""

pessoa = {}
dados = []
soma_idades = 0
mulheres = []
acima = []
while True:
  pessoa["Nome"] = str(input("Nome: "))
  pessoa["Sexo"] = str(input("Sexo:")).upper().strip()[0]
  if pessoa["Sexo"] == "F":
    mulheres.append(pessoa["Nome"])
  pessoa["Idade"] = int(input("Idade: "))
  soma_idades += pessoa["Idade"]
  while pessoa["Sexo"] not in "MF":
    print("Sexo invalido, so aceitamos M ou F")
    pessoa["Sexo"] = str(input("Sexo:")).upper().strip()[0]
  dados.append(pessoa.copy())
  cont = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
  if cont == "N":
    break
media = soma_idades / len(dados)

for pessoa in dados:
  if pessoa["Idade"] > media:
    acima.append(pessoa["Nome"])
print(f"foram cadastradas {len(dados)} pessoas")
print(f"A media de idade é {media} anos de idade")
print(f"As mulheres cadastradas foram: {mulheres}")
print(f"As pessoas acima da media de idade sao {acima}")
