# _*_ coding: utf-8 -*-
a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('É um número? ', a.isnumeric())
print('Só tem espaços? ', a.isspace())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())

# TODO: Refazer com a função print('{}'.format(k))
