u"""EXERCÍCIO060.

Curso de Python===>Professor Gustavo Guanabara--->ModuloII.

Faça um programa que leia um número qualquer e mostre seu fatorial.

Ex:
5! = 5x4x3x2x1 = 120
"""
'''from math import factorial
num = int(input('Digite um número para\ncalcular seu Fatorial:  '))
f = factorial(num)
print('O fatorial de {} é {}.'.format(num, f))'''
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
