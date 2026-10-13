"""
Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""

somaidade = 0
media_idade = 0
maior_idade_homem = 0
nomevelho = ""
totmulher20 = 0
for n in range(1,5):
  nome = str(input(f"Digite o nome da {n}ª pessoa: "))
  idade = int(input(f"Digite a idade da {n}ª pessoa: "))
  sexo = str(input(f"Informe o genero da {n}ª pessoa: F/M: "))
  somaidade = somaidade + idade
  if n == 1 and sexo in "Mm":
    maior_idade_homem = idade
    nomevelho = nome
  if sexo in "Mm" and idade > maior_idade_homem:
    maior_idade_homem = idade
    nomevelho = nome
  if sexo in "Ff" and idade < 20:
    totmulher20 += 1
media_idade = somaidade / 4
print(f"A media de idade do grupo é {media_idade}")
print(f"O homem mais velho tem {maior_idade_homem} e se chama {nomevelho}")
print(f"Ao todo sao {totmulher20} mulheres com menos de 20 anos")
