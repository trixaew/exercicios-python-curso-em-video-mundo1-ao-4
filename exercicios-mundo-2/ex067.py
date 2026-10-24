"""
Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""

while True:
  num = int(input("Digite um numero para ver a sua tabuada: "))
  if num < 0:
    break
  for i in range(1,11):
    print(f"{num} X {i} = {num * i}")
print("Programa encerado")
