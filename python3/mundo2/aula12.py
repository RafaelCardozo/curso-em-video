"""Aula 12 - parte prática."""

nome = str(input('Qual é o seu nome? '))
if nome == "Rafael":
    print('Que lindo nome!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Que belo nome femenino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
