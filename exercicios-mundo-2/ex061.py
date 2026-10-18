"""
Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

print("10 TERMOS DE UMA PA")
a = int(input("PRIMEIRO TERMO: ")) #
r = int(input("RAZÃO: "))
d = a + (10 - 1) * r
for c in range(a, d + r, r):
  print(c)
print("ACABOU")
