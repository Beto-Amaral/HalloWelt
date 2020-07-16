#desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

pri = int(input('primeiro termo: '))
razao = int(input('Razao: '))
decimo = pri + (10 - 1) * razao
for c in range(pri, decimo + razao, razao):
    print('{}'.format(c), end=' > ')
print('Acabou')

