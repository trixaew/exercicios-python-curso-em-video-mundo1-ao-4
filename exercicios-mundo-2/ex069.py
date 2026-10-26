"""
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
"""

total = 0
maior_idade = 0
mulher_20 = 0
homens = 0
while True:
  idade = int(input("Digite sua idade: "))
  sexo = str(input("Qual seu sexo: [M/F]")).upper().strip()
  total = total + 1

  if sexo == "F" and idade < 20:
    mulher_20 += 1

  if sexo == "M":
    homens += 1

  if idade >= 18:
    maior_idade += 1

  continuar = str(input("Quer continuar? [S/N]: ")).upper().strip()

  if continuar == "N":
    break
print(f"total é {total}, homens {homens}, maiores de idade {maior_idade}, mulheres menos de 20 {mulher_20}")
