"""
Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO
"""

nota = float(input("Informe sua 1ª nota: "))
nota2 = float(input("Informe a sua 2ª nota: "))
media = (nota + nota2) / 2
if media >= 5 and media < 7:
  print("Recuperação")
elif media >= 7:
  print("aprovado")
else:
  print("Reprovado")
