#  Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

#import math
#num = float(input('digite um valor: '))
#print('o valor digitado é {} e a porcao inteira é {}'.format(num, math.trunc(num)))

# ou para importar somente um método da bibllioteca por exemplo abaixo:

from math import trunc
num = float (input('Digite o valor: '))
print('o valor digitado é {} e a porcao inteira é: {}'.format(num, trunc(num)))