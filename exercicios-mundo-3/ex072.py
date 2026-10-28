"""
Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

tupla = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito",
"nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete",
"dezoito", "dezenove", "vinte")

while True:
  num = int(input("Digite um numero entre 0 e vinte: "))
  if num >= 0 and num <= 20:
    break
  print("Tente novamente")
print(f"Voce digitou o numero {tupla[num]}")
