"""
Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""

def area(larg, comp):
  a = larg * comp
  print(f"A area de um terreno {larg}X{comp} é de {a}m². ")

def t():
  print("-"*30)

print("CONTROLE TERRENOS")
t()
larg = float(input("Largura (m): "))
comp = float(input("Comprimento (m): "))
area(larg, comp)
