"""
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

contador = 0
soma = 0
paro = "Ss"
while paro != "N":
  num = int(input("Digite um numero: "))
  contador += 1
  soma = soma + num

  if contador == 1:
    maior = num
    menor = num
  else:
    if num > maior:
      maior = num
    if num < menor:
      menor = num
  paro = str(input("Quer continuar? [S/N]"))
media = soma /contador
print(f"Foram {contador} numeros digitados e a media é {media}, o maior numero é {maior} e menor {menor}")
