"""
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:

Quantos números foram digitados.
A lista de valores, ordenada de forma decrescente.
Se o valor 5 foi digitado e está ou não na lista.
"""

lista = []
while True:

  num = int(input("Digite um numero: "))
  lista.append(num)


  continuar = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
  if continuar == "N":
    break

lista.sort(reverse = True)
print(f"Foram digitados {len(lista)} elementos")

print(lista)

if 5 in lista:
  print("O numero 5 esta na lista")
else:
  print("o numero 5 nao esta na lista")
