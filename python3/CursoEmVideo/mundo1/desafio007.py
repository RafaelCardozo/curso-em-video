u"""Desafio007.

Crie um algoritmo que leia um número e mostre seu dobro, seu triplo e a raiz quadrada.
"""
n = int(input('Digite um número: '))
print('O número digitado foi {}.\n Seu dobro é {}.\n Seu triplo é {}.\n Sua raiz quadrada é {:.2f}'.format(
    n, n * 2, n * 3, n**(1 / 2)))
