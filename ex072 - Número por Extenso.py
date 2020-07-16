''' Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

cont = ('zero', 'um', 'Dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
        'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
        'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('dgite um num entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('tente novamente', end='')
print(f'O num digitao foi:', cont[num])
