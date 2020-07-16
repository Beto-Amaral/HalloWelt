#rie um programa que faça o computador jogar Jokenpô com você
print('JOGO')
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Quais as suas opcoes: 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(2)
print('PO')
print('-=' * 12)
print('O computador jogou: {}'.format(itens[computador]))
print('Jogador jogou: {}'.format(itens[jogador]))
print('-=' * 12)
if computador == 0: #computador jogou a pedra.
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('jogador Vence')
    elif jogador == 2:
        print('Computador Vence')
    else:
        print('Jogada Inválida')
elif computador == 1: #computador jogou Papel
    if jogador == 0:
        print('computador Vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('jogador vence')
    else:
        print('Jogada Inválida')
elif computador == 2: #computador jogou Tesoura.
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('computador Vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('jogada inválida')
