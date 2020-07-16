#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('OS segmentos podem formar triangulo' , end = '')
    if r1 == r2 == r3:
        print(' Equilátero')
    elif r1 != r2 != r3 != r1:
        print(' ESCALENO!')
    else:
        print(' Isóseles')
else:
    print('Os segmentos acima nao podem formar um triangulo')





