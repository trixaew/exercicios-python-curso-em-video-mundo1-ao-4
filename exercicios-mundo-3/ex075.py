"""
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
"""

valor = (int(input("Digite um valor: ")),
         int(input("Digite um valor: ")),
         int(input("Digite um valor: ")),
         int(input("Digite um valor:"))) #
print(f"Voce digitou {valor}")
print(f"O numero 9 aparece {valor.count(9)} vezes")
if 3 in valor:
  print(f"O numero 3 apareceu na {valor.index(3)+1} posicao ")
for par in valor:
  if par % 2 == 0:
    print(f"Os numero pares sao {par}")
