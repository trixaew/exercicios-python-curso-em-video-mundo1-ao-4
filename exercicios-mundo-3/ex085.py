"""
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""

numeros = [[], []]
for num in range(0,7):
  n = int(input(f"Digite o {num+1}º valor: "))
  if n % 2 == 0:
    numeros[0].append(n)

  else:
    numeros[1].append(n)

print(numeros)
numeros[0].sort()
numeros[1].sort()
print(f"Os numeros pares digitados foram {numeros[0]}")
print(f"Os numeros impares digitados foram {numeros[1]}")
