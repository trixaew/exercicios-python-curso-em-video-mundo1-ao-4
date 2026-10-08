"""
Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""

print("10 TERMOS DE UMA PA")
a = int(input("PRIMEIRO TERMO: "))
r = int(input("RAZÃO: "))
d = a + (10 - 1) * r
for c in range(a, d + r, r):
  print(c)
print("ACABOU")
