nota1 = float(input('Qual a primeira nota? '))
nota2 = float(input('Qual a segunda nota? '))

media = (nota1 + nota2) / 2
print('A media é: {:.1f}'.format(media))
if 7 > media >=5:
    print('O aluno esta em recuperacao.')
elif media < 5:
    print('O aluno esta reprovado.')
elif media >= 7:
    print('O aluno esta Aprovado.')