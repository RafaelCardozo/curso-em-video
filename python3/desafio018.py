u"""Décimo Oitavo Desafio."""
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(ca, co)
print('A hipotenusa mede {:.2f}'.format(hi))
