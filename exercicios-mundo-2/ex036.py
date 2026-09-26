"""
Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

casa = float(input("Qual o valor da casa: "))
salario = float(input("Qual o seu salario? "))
anos = int(input("Em quantos anos voce quer pagar? "))
prestacao = casa / (anos * 12)
minimo = salario * (30 / 100)
if prestacao <= minimo:
  print("Emprestimo foi concedido")
else:
  print("Emprestimo negado")
print(f"Para pagar uma casa de {casa}, em {anos} o valor da prestação sera {prestacao:.2f}")
