#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite o numero: '))
resultado = num % 2 #qdo se coloca a (%) por dois o resultado de qq numero vai dar 0 para n° pares e 1 para n° impares.
if resultado == 0:
    print('Este é um numero par')
else:
    print('este é um número ímpar')
