"""
Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

twice_shop = ("Candybong", 500.0,
              "This is for", 120.0,
              "Lil fantasy", 110.0,
              "Strategy", 120.0,
              "Zone", 110.0,
              "NA", 110.0,
              "Strategy hat", 60.0,
              "Lovely", 45.0,
              "Aboutzu", 110.0) 

print("----------TWICE SHOP----------\n")
for itens in range(0,len(twice_shop)):
  if itens % 2 == 0: 
    print(f"{twice_shop[itens]:.<30}", end=' ')
  else: 
    print(f"R${twice_shop[itens]:>6.2f}")
