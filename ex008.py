# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# km hm dam m dm cm mm

medida = float(input('Digite uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
print('o medida {} metros tem {:.0f}cm e {:.0f}mm'. format(medida, cm, mm))