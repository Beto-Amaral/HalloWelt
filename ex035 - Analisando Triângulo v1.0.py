#desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-==' * 20)
print('Anakisador de triangulos')
print('-==' * 20)
r1 = float(input('primeiro seguemento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Formam um trianngulo')
else:
    print('Nao formam um triangulo')

