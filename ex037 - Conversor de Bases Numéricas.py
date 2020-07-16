#Escreva um programa em Python que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um numero inteiro:'))
print('''Escolha uma das bases para conversao: 
[ 1 ] converter para Binário
[ 2 ] converter para Octal
[ 3 ] converter para Hexadecimal''')
if opcao == 1
    print('{} convertido para Binário é igual a {}'.format(num, bin(num)))