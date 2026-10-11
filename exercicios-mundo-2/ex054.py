"""
Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

import datetime
atual = datetime.date.today().year
maior = 0
menor = 0
for n in range(1,8):
  ano_nasci = int(input(f"Digite o ano de nascimento da {n}º: "))
  idade = atual - ano_nasci
  if idade >= 18:
    maior = maior + 1
  else:
    menor = menor + 1
print(f"Ao todo tivemos {maior} pessoas maiores de idade e {menor} pessoas menores de idade")
