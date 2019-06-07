u"""EXERCÍCIO063.

Curso de Python===>Professor Gustavo Guanabara--->ModuloII.

Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
Ex:
0 ¬ 1 ¬ 1 ¬ 2 ¬ 3 ¬ 5 ¬ 8
"""
print('-' * 30)
print('Sequência de Fibonacci!')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print('{} ¬ {}'.format(t1, t2), end='')
count = 3
while count <= n:
    t3 = t1 + t2
    print(' ¬ {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    count += 1
print('¬ FIM')
print('~' * 30)
