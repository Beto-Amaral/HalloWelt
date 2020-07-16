# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Onde vc nasceu? ')).strip()
print(cidade[0:5].upper() == 'SANTO')