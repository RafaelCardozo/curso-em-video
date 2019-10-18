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

# TODO: Refazer o código com a função print no formato python3.
# Ex.: print('{}'.format(k))
