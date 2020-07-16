'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''

peso = float(input('Qual o peso? (Kg) ' ))
alt = float(input('Qual a altura? (m)'))
imc = peso / (alt ** 2)
print('Seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobre peso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade Morbida')


