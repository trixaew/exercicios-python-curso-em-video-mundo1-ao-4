"""
Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""

a = float(input("Informe o valor da reta 1: "))
b = float(input("Informe o valor da reta 2: "))
c = float(input("Informe o valor da reta 2: "))
if a + b > c and a + c > b and b + c > a:
  print ("Da para formar um triangulo")
else:
  print("Nao da para formar um triangulo")
