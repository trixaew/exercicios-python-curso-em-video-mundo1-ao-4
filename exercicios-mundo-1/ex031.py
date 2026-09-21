"""
Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R 0,5 0por Km para viagens de até 200Km R$0,45 parta viagens mais longas.
"""

distancia = float(input("Informe a distancia da viagem: "))
if distancia > 200:
  print(f"Voce vai pagar {distancia*0.45}")
else:
  print(f"Voce vai pagar {distancia*0.50}")
