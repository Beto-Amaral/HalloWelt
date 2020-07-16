#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar
# ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Voce tem que se alistar imediatamente')
elif idade < 18:
    saldo = 18 - idade
    print('Voce ainda nao tem 18 anos, faltam {} anos para voce se alistar'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce ja devia ter feito o alistamento há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))





