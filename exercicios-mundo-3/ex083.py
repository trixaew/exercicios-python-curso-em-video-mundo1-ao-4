"""
Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

expressao = str(input("Digite uma expressao: "))
cont = 0
for contador in expressao:
  if contador == "(":
    cont += 1
  elif contador == ")":
    cont -= 1
    if cont < 0:
      break

if cont == 0:
  print("Expressao valida")
else:
  print("Expressao invalida")
