u"""Desafio011.

Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
Considere - US$1,00 = R$3,27
"""
c = float(input('Quanto dinheiro você tem na carteira? R$'))
d = 3.27
print('Com R${:.2f}, podes comprar US${:.2f}'.format(c, c/d))

# TODO: Acrescentar a conversão para Yene, Euro, Libra Isterlina, Peso Colombiano, e todos os paises que já fui.
