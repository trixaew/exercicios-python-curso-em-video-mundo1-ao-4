"""
Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

contador = 0
numero = int(input("Digite um numero: "))
for n in range(1, numero + 1): 
  if numero % n == 0: 
    contador = contador + 1
print(f"O numero {numero} foi divisivel {contador} vezes")
if contador == 2: 
  print("numero primo")
else:
  print("numero nao é primo")
print(contador, n)
