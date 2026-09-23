"""
Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

a = float(input("Informe um valor: "))
b = float(input("Informe um valor: "))
c = float(input("Informe um valor: "))
if a > b and a > c:
  maior = a
if b > a and b > c:
  maior = b
if c > a and c > b:
  maior = c
if a < b and a < c:
  menor = a
if b < a and b < c:
  menor = b
if c < a and c < b:
  menor = c
print(f"O menor valor digitado foi: {menor}")
print(f"O maior valor digitado foi: {maior} ")
