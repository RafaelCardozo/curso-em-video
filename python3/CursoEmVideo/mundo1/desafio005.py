u"""Desafio005.

Faça um programa que leia algo pelo teclado e
 mostre na tela o seu tipo primitivo e todas as informações possíveis sobre
 ele.
"""
a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('É um número? ', a.isnumeric())
print('Só tem espaços? ', a.isspace())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())


b = input('Digite algo novamente: ')
print('O tipo primitivo de {} é {}'.format(b, type(b)))
print('{} é alfabético? {}'.format(b, b.isalpha()))
print('{} é alfanumérico? {}'.format(b, b.isalnum()))
print('{} é um número? {}'.format(b, b.isnumeric()))
print('{} só tem espaços? {}'.format(b, b.isspace()))
print('{} está em maiúsculas? {}'.format(b, b.isupper()))
print('{} está em minúsculas? {}'.format(b, b.islower()))
print('{} está capitalizada? {}'.format(b, b.istitle()))
