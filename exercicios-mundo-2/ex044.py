"""
Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros
"""

preco = float(input("Qual o preço das compras? "))
print("[ 1 ] - À vista dinheiro/cheque ")
print("[ 2 ] - À vista no cartão  ")
print("[ 3 ] - Em 2x no cartão ")
print("[ 4 ] - 3x ou mais no cartão ")
opcao = int(input("Qual a opção: "))
din = preco - (preco * 0.1)
cartao = preco - (preco * 0.05)
total = preco + (preco * 0.2)
if opcao == 1:
  print(f"O preço é de {preco} mas com o desconto de 10% o valor sera {din}")
elif opcao == 2:
  print(f"O preço é de {preco} mas com o desconto de 5% o valor sera {cartao}")
elif opcao == 3:
  print(f"O preço é de {preco} mas como sera parcelado, o valor das percelas sera {preco/2} ")
elif opcao == 4:
  parcelas = int(input("Qual o total de parcelas? "))
  tot = total/parcelas
  print(f"Sua compra sera parcelada em {parcelas} vezes de {tot} com 20% de juros")
  print(f"O preço é de {preco} mas como ha juros, o valor total do produto sera {total}")
else:
  print("Opção invalida")
