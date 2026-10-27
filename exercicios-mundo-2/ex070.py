"""
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
"""

total = 0
mais = 0
menor = 0
print("LOJA DO TWICE")
while True:
  produto = str(input("Qual o nome do produto? "))
  preco = float(input("Qual o valor do produto? "))
  total = total + preco

  if preco > 1000:
    mais += 1

  if total == preco or preco < menor:
    menor = preco
    nome_menor = produto


  continuar = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]
  if continuar == "N":
    break
print(f"O total é {total}, o menor preço é {nome_menor} custando {menor} e {mais} item custa mais de 1000 reais")
