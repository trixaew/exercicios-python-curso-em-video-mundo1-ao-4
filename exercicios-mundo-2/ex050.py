"""
Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""

par = 0
qts = 0
for n in range(1,7):
  numeros = int(input(f"Digite o {n} º numero: "))
  qts = qts + 1
  if numeros % 2 == 0:
    par = par + numeros
print(f"Voce infornou {qts} numeros e a soma dos numeros pares digitados é {par}")
