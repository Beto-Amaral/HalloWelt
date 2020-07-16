# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('qual o seu salario? R$: '))

novo_salario = salario + (salario * 15 / 100)
print('novo salario: {:.3f} '.format(novo_salario))


