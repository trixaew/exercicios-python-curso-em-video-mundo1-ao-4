"""
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

info = {}
info["Nome"] = str(input("Nome: "))
info["Partidas"] = int(input("Partidas jogadas: "))

info["Gols"] = []
for partida in range(info["Partidas"]):
  info["Gols"].append(int(input(f"Quantos gols foram feitos na partida {partida+1}? ")))
info["Total"] = sum(info["Gols"])
print("=-"*30)
print(info)
print("=-"*30)
for k, v in info.items():
  print(f"No campo {k} achei {v}")
print("=-"*30)
print(f"O jogador {info["Nome"]} jogou {info["Partidas"]} partidas.")
for partida in range(info["Partidas"]):
  print(f"Na partida {partida+1} fez {info["Gols"][partida]} gols")
print(f"Foi um total de {info["Total"]} gols")
