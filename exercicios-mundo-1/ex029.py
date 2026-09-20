"""
Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""

velo = float(input("Informe a velocidade do seu carro em KM: "))
if velo > 80:
  multa = (velo - 80) * 7
  print(f"Voce passou a velocidade permitida e sera multado em {multa} R$")
else:
  print("Voce não foi multado, PARABENS!")
