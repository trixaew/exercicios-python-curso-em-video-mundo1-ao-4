"""
Exercício Python 087: Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.
"""

par = 0  
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 

for linha in range(0,3): 
  for coluna in range(0,3):  
    matriz[linha][coluna] = int(input("Escreva um valor: ")) 
    if matriz[linha][coluna] % 2 == 0: 
      par += matriz[linha][coluna] 

for linha in range(0,3): 
  for coluna in range(0,3):   
    print(f"[{matriz[linha][coluna]:5^}]", end='') 
  print() 

soma_t = 0 
for linha in range(0,3): 
  soma_t += matriz[linha][2]  
  

maior_num = matriz[1][0] 

for coluna in range(0,3): 
  if matriz[1][coluna] > maior_num: 
 
    maior_num = matriz[1][coluna]


print(f"A soma dos valores pares sao {par}")
print(f"A soma dos valores {soma_t}")
print(f"O maior valor da segunda linha é {maior_num}")
