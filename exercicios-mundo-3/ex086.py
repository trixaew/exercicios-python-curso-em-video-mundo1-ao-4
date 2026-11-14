"""
Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
"""

matriz = [[1, 2, 3,],
          [4, 5, 6,],
          [7, 8, 9,]]

for linha in matriz:
    for valor in linha:
        print(f"[{valor:}]", end="")
    print()
