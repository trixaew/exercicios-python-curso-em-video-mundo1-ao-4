"""
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import randint 

mega = [] 
dados = [] 


jogos = int(input("Quantos jogos? ")) 
for jogo in range(jogos): 

  while len(dados) < 6: 
    num = randint(1,60) 
    if num not in dados: 
      dados.append(num) 
      dados.sort() 
  mega.append(dados[:]) 
  dados.clear() 

for jogo in mega: 
  print(jogo) 
