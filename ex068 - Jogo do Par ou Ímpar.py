from random import randint
while True:
    jogador = int(input('digite um numero: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = str(input('Par ou ímpar? '))
    print(f'voce jogou {jogador} e o computador {computador}. Total de {total}')

