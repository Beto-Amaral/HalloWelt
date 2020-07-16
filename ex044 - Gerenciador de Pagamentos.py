'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

print('{:=^40}'.format(' Lojas Amaral '))
preco = float(input('Preco das comprar:R$ '))
print('''Formas de pagamento
[ 1 ] à vista dinheiro ou cheque
[ 2 ] à vista no cartao
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao. 
''')
opcao = int(input('Qual a forma de pagamento?  '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = preco / 2
    print('Sua compra no valor de R${:.2f} sera parcelada em 2x no valor de R${:.2f}'.format(preco, parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparcela = int(input('Em quantas parcelas? '))
    parcela = total / totparcela
    print('Sua compra será parcelada em {} de R${:.2f} com juros'.format(totparcela, parcela))

print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(preco, total))

