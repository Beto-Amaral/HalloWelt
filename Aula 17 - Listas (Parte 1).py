'''valores = [11, 13, 14, 4, 5, 6, 7, 8, 9, 10]
valores[0] = 23
valores.append(33)
valores.sort(reverse=True)
valores.insert(2, 2)
valores.insert(0, 2)
if 24 in valores:
    valores.remove(24)
else:
    print('Nao achei o numero 24')
print('-' * 40)
valores.remove(2)
print(valores)
print(f'esta lista tem {len(valores)} elementos')
print('~' * 40)
print('Bom trabalho garoto!!')'''
valores = []
'''valores.append(5)
valores.append(9)
valores.append(4)'''
'''for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}')
print('Cheguei ao final da lista!! Bom trabalho meu jovem!')'''

a = [2, 3, 4, 5, 7]
b = a[:] # significa que b recebe uma copia dos valores de a
b[2] = 8 # mudar a posicao 2 do b para 8
print(a)
print(b)












