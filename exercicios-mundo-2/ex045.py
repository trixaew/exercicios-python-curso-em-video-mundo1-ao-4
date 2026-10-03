"""
Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
"""

import random
print("Suas opções:")
print("[ 1 ] - Pedra ")
print("[ 2 ] - Papel ")
print("[ 3 ] - Tesoura ")
opcoes = [1 , 2 , 3]
escolha = random.choice(opcoes)
jogada = int(input("Qual a sua jogada? "))
nome = ["pedra", "papel", "tesoura"]
print(f"Você jogou: {nome[jogada - 1]}")
print(f"Computador jogou: {nome[escolha - 1]}")
if jogada == escolha:
  print(f"Empataram pois ambos jogaram {nome[jogada - 1]} e {nome[escolha - 1]}")
elif jogada == 1 and escolha == 3:
  print("Jogador ganhou!")
elif jogada == 2 and escolha == 1:
  print("Jogador ganhou!")
elif jogada == 3 and escolha == 2:
  print("Jogador ganhou!")
else:
  print("Computador venceu")
