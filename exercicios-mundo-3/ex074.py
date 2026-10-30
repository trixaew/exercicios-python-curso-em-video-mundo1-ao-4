"""
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

from random import randint


ale = tuple(randint(1,100) for i in range(5))
print(ale)
print(f"O menor valor é {min(ale)} e o maior é {max(ale)}")
