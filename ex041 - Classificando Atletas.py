'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade =  atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('O atleta é mirin.')
elif idade <= 14:
    print('É um atleta infantil')
elif idade <= 19:
    print('O atleta é Júnior')
elif idade <= 25:
    print('O atleta é Senior.')
elif idade > 25:
    print('O atleta é Master.')
