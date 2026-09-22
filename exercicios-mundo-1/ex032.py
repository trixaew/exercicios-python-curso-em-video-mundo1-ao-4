"""
Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""

import datetime
ano = int(input("Qual ano voce quer analisar? Se quiser analisar esse ano clique 0 "))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 ==0  and ano % 100 != 0 or ano % 400 == 0:
  print(f"O ano é bissexto {ano}")
else:
  print(f"O ano nao é bissexto {ano}")
