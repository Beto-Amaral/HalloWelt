#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))

media_da_nota = (nota1 + nota2) / 2

print('A media entre {:.1f} e {:.1f} é de: {:.1f} '.format(nota1, nota2, media_da_nota))