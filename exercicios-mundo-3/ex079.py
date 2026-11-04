"""
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

lista = []
num = int(input("Digite um valor: "))
lista.append(num)
continuar = input("Deseja continuar? [S/N] ").upper().strip()[0]

while continuar != "N":
  num = int(input("Digite um valor: "))

  if num not in lista:
    lista.append(num)
  else:
    print("Numero ja existe na lista, nao vou adicionar")
  continuar = input("Deseja continuar? [S/N] ").upper().strip()[0]
lista.sort()
print(lista)
