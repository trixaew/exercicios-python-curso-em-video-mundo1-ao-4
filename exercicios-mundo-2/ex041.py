"""
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
"""

import datetime
ano = int(input("Informe o ano que voce nasceu: "))
idade = datetime.date.today().year - ano
print(idade)
if idade < 10:
  print("MIRIM")
elif idade >= 10 and idade < 15:
  print("INFANTIL")
elif idade >= 15 and idade < 20:
  print("JUNIOR")
elif idade >= 20 and idade < 25:
  print("SENIOR")
else:
  print("MASTER")
