"""
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
"""

times = ("Palmeiras", "Flamengo", "Fluminense", "Athletico-PR", "Bragantino", "Coritiba", "São Paulo", "Bahia", "Cruzeiro", "Botafogo", "Vitória", "Atlético-MG",
         "Internacional", "Grêmio", "Corinthians", "Vasco", "Santos", "Mirassol", "Remo", "Chapecoense")
print(f"Os cinco primeiros times sao: {times[0:5]}")
print(f"Os quatro ultimos colocados são: {times[16:20]}")# {times[-4:]}
print(sorted(times))
print(f"A Chapecoense esta na posição: {times.index("Chapecoense")+1}ª")
