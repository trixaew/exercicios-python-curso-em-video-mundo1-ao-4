"""
Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""

import random
print("Acabei de pensar em um numero de 0 a 10! ")
print("Será que você consegue advinhar?... ")
contador = 0
n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolha = random.choice(n)
numero = int(input("Escolha um numero entre 0 e 10: "))
contador = contador + 1
while numero != escolha:
  if numero < escolha:
    print("Numero muito baixo")
  else:
    print("Numero muito alto")
  numero = int(input("Errou! tente novamente "))
  contador = contador + 1
print(f"Voce acertou em {contador} tentativas")
