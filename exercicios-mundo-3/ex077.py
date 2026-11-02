"""
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

palavras = ("Nayeon", "Jeongyeon", "Momo", "Sana", "Jihyo", "Mina", "Dahyun", "Chaeyoung", "Tzuyu", "Twice")
for palavra in palavras: 
  print(f"\n Na palavra {palavra.upper()} temos ", end = '')
  for letras in palavra: 
    if letras.lower() in "aeiou":
      print(letras, end=' ')
