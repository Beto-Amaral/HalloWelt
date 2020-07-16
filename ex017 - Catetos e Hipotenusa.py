# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

# vou importar o metodo math para o calculo de hipotenusa.
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do catoto adjacente: '))
hi = math.hypot(co, ca)
print('Valor da hipotenusa: {}'.format(hi))



