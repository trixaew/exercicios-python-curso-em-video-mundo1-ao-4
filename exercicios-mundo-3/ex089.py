"""
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

notas = []
dados = []
soma = 0
while True:
  dados.append(str(input("Nome do aluno: ")))
  dados.append(float(input("Nota 1: ")))
  dados.append(float(input("Nota 2: ")))
  notas.append(dados[:])
  dados.clear()
  cont = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
  if cont == "N":
    break

for posi, aluno in enumerate(notas):
  media = (aluno[1] + aluno[2])/2
  print(f"{posi} NOME: {aluno[0]}  MEDIA: {media}")

while True:
  escolha = int(input("Mostrar a nota de qual aluno? 999 para parar "))
  if escolha == 999:
    break

  print(f" notas de {notas[escolha][0]} sao [{notas[escolha][1]}, {notas[escolha][2]}] ")
