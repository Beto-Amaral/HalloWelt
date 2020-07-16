# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador 'pensar' e escolher o número
print('-=-' * 25)
print('Eu, computador, vou pensar em um numero de 0 a 5, tente adivinhar')
print('-=-' * 25)
jogador = int(input('em que número eu pensei? ')) # o jogador tenta adivinhar.
print('PROCESSANDO...')
sleep(3) #funcao para esperar o resultado por 3 segundos. E só depois vem o resultado.
if jogador == computador:
    print('Parabens, voce conseguiu vencer.')
else:
    print('Ganhei! Eu pensei no número {} e nao no {}'.format(computador, jogador))
