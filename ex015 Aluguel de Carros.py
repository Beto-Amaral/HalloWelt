# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = int(input('quantos km rodados? '))
dias = int(input('quanto dias alugados? '))
total = (km * 0.15) + (dias * 60)
print('quantidade rodados foi {}Km, e a quantidade de dias foi {}, e o preco a pagar é de R${:.2f}'.format(km, dias, total ))