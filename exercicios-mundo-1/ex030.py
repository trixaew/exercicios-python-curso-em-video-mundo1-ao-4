"""
Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""
n = int(input("Digite um numero inteiro: "))
resultado = n % 2
if resultado == 0:
  print("Seu numero é par")
else:
  print("seu numero é impar")
