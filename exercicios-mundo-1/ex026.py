"""
Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
"""

frase = str(input("Digite uma frase: ")).strip()
print(f"A letra A aparece {(frase.count('a'))} vezes \n A primeira letra A apareceu na posição {(frase.find('a')+1)} \n A ultima letra A apareceu na posição {(frase.rfind('a')+1)}")
