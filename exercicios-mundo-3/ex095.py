"""
Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

info = {}
dados = list()

while True:
  info["Nome"] = str(input("Nome: "))
  info["Partidas"] = int(input("Partidas: "))
  info["Gols"] = []
  for partida in range(info["Partidas"]):
    info["Gols"].append(int(input(f"Quantos gols foram feitos na partida {partida+1}: ")))
  info["Total"] = sum(info["Gols"])
  dados.append(info.copy())

  cont = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
  if cont == "N":
    break

print("=-" *30)

print(f"{"Cod":<4} {"Nome":<10}{"Gols":<10}{"Total":>8} ")
print("=-"*26)
for pos, jogador in enumerate(dados):
  print(f"{pos:<4} {jogador['Nome']:<10} {jogador['Gols']} {jogador['Total']:>8}")
while True:
  print("=-"*30)
  escolha = int(input("Mostrar dados de qual jogador? (999 para encerrar) "))
  if escolha == 999:
    break
  if escolha >= len(dados):
    print("Erro! Nao existe jogador com esse codigo")
  for partida, gol in enumerate(dados[escolha]["Gols"]):
    print(f"Na partida {partida+1} fez {gol} gols")
