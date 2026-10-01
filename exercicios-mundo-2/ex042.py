"""
Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
"""

lado = float(input("Informe o valor da reta 1: "))
lado2 = float(input("Informe o valor da reta 2: "))
lado3 = float(input("informe o valor da reta 3: "))
if lado == lado2 == lado3:
  print("Equilatero")
elif lado != lado2 != lado3:
  print("ESCALENO")
else:
  print("ISOSCELES")
