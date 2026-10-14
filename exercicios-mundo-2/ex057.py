"""
Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = str(input("Digite um sexo: [M/F] ")).lower()
while sexo != "m" and sexo != "f":
  sexo = input("Codigo invalido! Digite novamente: ").lower()
print("Sexo registrado com sucesso! ")
