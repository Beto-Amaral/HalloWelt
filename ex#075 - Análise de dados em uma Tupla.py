'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

num = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('digite umais um valor: ')),
      int(input('Digite o ultimo numero: ')))
print('voce digitou o valores', {num})
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 foi digitado na {num.index(3)+1} posicao')
else:
    print('O valor 3 nao foi digitado em nenhuma posicao:')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
