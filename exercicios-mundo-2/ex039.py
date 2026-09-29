"""
Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

import datetime
ano = int(input("Informe o seu ano de nascimento: "))
idade = datetime.date.today().year - ano 
print(f"Voce tem {idade} anos")
if idade < 18:
  print(f"Voce não precisa se alistar, pois ainda faltam {18 - idade} ano(s)")
elif idade == 18:
  print(f"Você PRECISA se alistar esse ano")
else:
  print(f"Ja passou o tempo do alistamento! voce deveria ter se alistado em {datetime.date.today().year - (idade - 18)}")

