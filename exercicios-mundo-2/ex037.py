"""
Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""

num = int(input("Escreva um numero inteiro: "))
print("1 - Converter para binario")
print("2 - Converter para octal")
print("3 - Converter para hexadecimal")
escolha = int(input("[1, 2 ou 3] "))
if escolha == 1:
  print(f"O valor convertido em binário é {bin(escolha)}")
elif escolha == 2:
  print(f"O valor convertido em octal é {oct(escolha)}")
elif escolha == 3:
  print(f"O valor convertido em hexadecimal é {hex(escolha)}")
else:
  print("Opção invalida")
