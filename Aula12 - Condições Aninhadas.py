# vamos aprender como criar estruturas condicionais aninhadas, usando os comandos if.. elif.. else em programas Python.

nome = str(input('Qual o seu nome? '))
if nome == 'Roberto':
    print('Que nome bonito!!')
elif nome == 'Pedro' or nome == 'Paulo' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cory Fernanda Cristina':
    print('Que belo nome feminino.')
else:
    print('Seu nome é bem normal! ')
print('Tenha um bom dia, {}!!'.format(nome))
