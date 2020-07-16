#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.

nome = str(input('qual o seu nome completo? ')).strip()
print('analisando o seu nome...')
print('seu nome em maiusculas é {}'.format(nome.upper()))
print('seu nome em minusculo é: {}'.format(nome.lower()))
print('seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))


