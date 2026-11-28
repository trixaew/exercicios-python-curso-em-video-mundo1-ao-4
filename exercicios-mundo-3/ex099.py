"""
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior
"""

def maior(* numeros):
  big = max(numeros)
  for n in numeros:
    print(n,end=' ')
  print(f"Foram informados {len(numeros)} valores no total. O maior valor é {big}")



maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
