#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário
# ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa? R$ '))
salário = float(input('qual o seu salario? R$'))
anos = int(input('Em quantos anos de financiamento? R$'))
prestacao = casa / (anos * 12)
minimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f}, em {} anos a pretacao sera de R${:.2f}'.format(casa, anos, prestacao))
if prestacao <= minimo:
    print('Alles gut, pode liberar.')
else:
    print('Nao vai rolar bonitao')



