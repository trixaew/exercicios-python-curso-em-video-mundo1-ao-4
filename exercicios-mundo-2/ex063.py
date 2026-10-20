"""
Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
"""

termo = 0
termo_1 = 1
contador = 3
numero = int(input("Digite um numero: "))
print(termo)
print(termo_1)
while contador <= numero:
  termo_3 = termo + termo_1
  print(termo_3)
  termo = termo_1
  termo_1 = termo_3
  contador += 1
