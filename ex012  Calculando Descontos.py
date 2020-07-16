# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o valor do produto '))

novo_valor = preco - (preco * 5 / 100)


print('O preco com desconto é: {}'.format(novo_valor))