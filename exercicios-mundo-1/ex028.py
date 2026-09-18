"""
Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

import random
num = int(input("Escolha um numero entre 0 e 5: "))
n = [0, 1, 2, 3, 4, 5]
escolha = random.choice(n)
if escolha == num:
  print("Parabens voce acertou")
else:
  print("Voce errou")
print(f"O numero escolhido foi: {escolha}")



