#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\33[31m', end='')
    print('{}'.format(c), end='')
print('\n\033[meu numero {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso que ele é PRIMO!')
else:
    print('è por qiosso que ele NAO é primo!')


