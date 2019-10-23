u"""Desafio015.

Escreva um programa que converta uma temperatura digitada em ºC e coneverta para F.
"""
c = float(input('Informe a temepratura em ºC: '))
f = 9 * c / 5 + 32
print('A temperatura de {}ºC corresponde a {}ºF!'.format(c, f))
