"""
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R 50,R 20, R 10eR 1.
"""


print("ATM JIHYO RAINHA")
while True:
  valor = int(input("Qual sera o valor sacado? R$: "))
  ced50 = valor // 50
  valor = valor % 50

  ced20 = valor // 20
  valor = valor % 20

  ced10 = valor // 10
  valor = valor % 10

  ced1 = valor // 1
  valor = valor % 1
  print(f"Vao ser sacado {ced50} notas de 50, {ced20} notas de 20, {ced10} notas de 10 e {ced1} notas de 1")

  continuar = str(input("[S/N]"))
  if continuar == "N":
    break
