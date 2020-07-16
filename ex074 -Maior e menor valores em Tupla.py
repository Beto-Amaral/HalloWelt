'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint
numeros = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print(f'Os numeros sorteados foram: {numeros}')
print(f'O maior num é: {max(numeros)}')
print(f'o menor numero é: {min(numeros)}')