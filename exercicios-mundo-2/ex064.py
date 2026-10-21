"""
Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""

qtd = 0
soma = 0
num = int(input("Digite um numero: "))
while num != 999:
  qtd += 1
  soma = soma + num
  num = int(input("Digite um numero: "))
print(f"A quantidade de numeros digitados foi {qtd} e a soma foi {soma}")
