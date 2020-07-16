'''Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''
total = totmil = menor = cont = 0
barato = ''
while True:
    nome = str(input('Qual o nome do produto? '))
    preco = float(input('Qual o preco? R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'o Total da compra foi: R${total:.2f}')
print(f'quantidade produtos que custam mais de R$1000: {totmil}')
print(f'O prod mais barato foi {barato} que custa R${menor:.2f}')


