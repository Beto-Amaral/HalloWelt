# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
n1 = str(input('Primeiro nome: '))
n2 = str(input('segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('quarto nomne: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('o none ecolido foi : {} '.format(escolhido))
