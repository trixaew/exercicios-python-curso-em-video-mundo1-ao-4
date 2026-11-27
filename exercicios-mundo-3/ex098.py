"""
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada: a) de 1 até 10, de 1 em 1 b) de 10 até 0, de 2 em 2 c) uma contagem personalizada
"""

import time
def contador(inicio, fim, passo):
  if passo == 0:
    passo = 1
  if inicio < fim:
    for c in range(inicio, fim +1, abs(passo)):
      time.sleep(0.5)
      print(c, end='  ')

  else:
    for c in range(inicio, fim -1, -abs(passo)):
      time.sleep(0.5)
      print(c, end='  ')




print("Contagem 1 ate 10")
contador(1, 10, 1)
print()
print("Contagem de 10 ate 0")
contador(10, -1, -2)
print()
print("Agora é sua vez de personalizer")
i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passos: "))
contador(i,f,p)
