'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

valores = []
while True:
    valores.append(int('Digite um valor: '))
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break
