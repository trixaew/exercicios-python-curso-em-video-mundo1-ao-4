"""
Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
"""

info = {}
dados = []
info["Nome"] = str(input("Nome: "))
info["Media"] = float(input("Media: "))
if info["Media"] >= 7:
  info["Situação"] = "Aprovado(a)"
elif info["Media"] >= 5:
  info["Situação"] = "Recuperação"
else:
  info["Situação"] = "Reprovado(a)"
dados.append(info.copy())

for k, v in info.items():
  print(f" - {k} é igual a {v}")
