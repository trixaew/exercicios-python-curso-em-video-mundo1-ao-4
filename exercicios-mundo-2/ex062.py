"""
Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
"""

from time import sleep
termo = 1
termo_1 = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
while termo <= 10:
  print(f"{termo}º termo = {termo_1}")
  termo_1 = termo_1 + razao
  termo += 1
adicionar = int(input("Deseja adicionar mais termos? "))
while adicionar != 0:
  contador = 1
  while contador <= adicionar:
    print(f"{termo}º = {termo_1}")
    termo_1 = termo_1 + razao
    termo = termo + 1
    contador += 1

  adicionar = int(input("Deseja adicionar mais termos? "))
print("FINALIZANDO...")
sleep(1)
print(f"FIM foram mostrados {termo-1} no total")
