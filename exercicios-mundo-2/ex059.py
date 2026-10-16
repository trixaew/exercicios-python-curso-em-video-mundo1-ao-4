"""
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""

from time import sleep

operacao = 0
while operacao != 5:
  valor = int(input("Digite o primeiro valor: "))
  valor2 = int(input("Digite o segundo valor: "))
  print("[1] - SOMAR ")
  print("[2] - MULTIPLICAR ")
  print("[3] - MAIOR ")
  print("[4] - NOVOS NUMEROS ")
  print("[5] - SAIR DO PROGRAMAR")
  operacao = int(input("Qual operação voce escolhe? "))
  if operacao == 1:
    soma = valor + valor2
    print(f"A soma dos valores é {soma}")
  elif operacao == 2:
    multiplicacao = valor * valor2
    print(f"A multiplicação do valores é {multiplicacao}")
  elif operacao == 3:
    if valor > valor2:
      print(f"{valor} é maior")
    else:
      print(f"{valor2} é maior")
  elif operacao == 4:
    print("Informe os numeros novamente")
    valor = int(input("Primeiro valor: "))
    valor2 = int(input("Segundo valor: "))
  elif operacao == 5:
    print("Finalizando...")
  else:
    print("Operação invalida. Tente novamente")
  print('=-=' * 10)
  sleep(1)
print("FIM DO PROGRAMA")
