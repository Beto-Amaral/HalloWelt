'''n = int(input('Digite até que numero voce gostaria que a conta fosse: '))
for c in range(n, -1, -1):
    print(c)
print('FIM')'''

'''i = int(input('Inicio '))
f = int(input('FIM '))
p = int(input('Passo '))
for c in range(i, f+1, p):
    print(c)
print('FIM')'''

S = 0
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    S += n
print('Somatório de todos os valores foi {}.'.format(S))