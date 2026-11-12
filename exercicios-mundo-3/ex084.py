"""
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.
"""

pessoas = list()
dados = list()
while True:
  dados.append(str(input("Digite seu nome: ")))
  dados.append(float(input("Digite seu peso: ")))
  pessoas.append(dados[:])
  dados.clear()

  conti = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
  if conti == "N":
    break

pesadas = pessoas[0][1] #pesadas recebe o peso da primeira pessoa
leves = pessoas[0][1] #leves recebe o peso da primeira pessoa

for pessoa in pessoas: #para cada pessoa em pessoas (lista pessoas)
  if pessoa[1] > pesadas: #se o peso da pessoa for maior que o maior peso encontrado até agora
    pesadas = pessoa[1] # atualiza o maior peso

  if pessoa[1] < leves: #mesma coisa com o leves
    leves = pessoa[1]

mais_pesadas = [] #lista de pessoas mais pesadas
for pessoa in pessoas: #para cada pessoa em pessoas (lista pessoas)
    if pessoa[1] == pesadas: # verifica quem possui o maior peso
      mais_pesadas.append(pessoa[0]) #adiciona o NOME da pessoa na lista de mais pesadas


mais_leves = [] #mesma coisa com a lista mais leves
for pessoa in pessoas:
    if pessoa[1] == leves:
      mais_leves.append(pessoa[0])

print(f"Foram cadastradas {len(pessoas)} pessoas")
print(f"As pessoas mais pesadas sao {mais_pesadas}")
print(f"As pessoas mais leves sao {mais_leves}")
