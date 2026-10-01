"""
Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
"""

peso = float(input("Informe o seu peso: "))
altura = float(input("informe a sua altura: "))
imc = peso / (altura * altura)
print (f"Seu imc é {imc:.2f}")

if imc < 18.5:
  print("Você esta ABAIXO DO PESO")
elif imc >= 18.5 and imc <= 25:
  print("Voce esta no PESO IDEAL")
elif imc > 25 and imc <= 30:
  print("Voce esta em SOBREPESO")
elif imc > 30 and imc <= 40:
  print("Voce esta em OBESIDADE")
else:
  print("Voce esta em OBESIDADE MORBIDA, CUIDADO!")
