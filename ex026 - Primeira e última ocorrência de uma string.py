#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('digite a sua frase: ')).upper().strip()
print('A letra A aparece {} na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posicao {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu nao posicao: {}'.format(frase.rfind('A')+1))2