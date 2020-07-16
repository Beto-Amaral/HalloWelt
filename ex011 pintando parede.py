# : Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,


larg = float(input('largura da parede'))
alt = float(input('Altura da parede'))
area = larg * alt
print('Sua parede tem a dimensao de {}x{} e sua area é de {}m².'.format(larg, alt, area))
tinta = area / 2 # sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
print('Voce vai precisar de {}l de tinta para pintar.'.format(tinta))
