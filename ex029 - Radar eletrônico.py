#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

velo = float(input('Qual é a velocidade do carro? '))

if velo > 80:
    print("Multado! Voce esta acima do limite permitido que é de 80Km/h.")
    multa = (velo - 80) * 7
    print('Voce deve pagar a multa de R${:.2f}'.format(multa))
else:
    print('Dirija com seguranca! ')
print('Tenha um bom dia!')

velo = float(input('Qual é '))