"""
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

valores = []

for n in range(5):
  valores.append(int(input(f"Digite o {n} valor: ")))

maior = max(valores)
menor = min(valores)
print(f"Voce digitou os valores {valores}")

for posi, n in enumerate(valores):
    print(f"Na posicao {posi} encontrei o valor {n}")
    if n == maior:
      print(f"maior valor encontrado na posicao {posi}")
    if n == menor:
      print(f"menor valor encontrado na posicao {posi}")
print(f"O maior valor é {maior} e o menor é {menor}")
