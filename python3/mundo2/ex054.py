u"""EXERCÍCIO053.

Curso de Python===>Professor Gustavo Guanabara--->ModuloII.

Crie um programa que leia uma frase qualquer e diga se ela é
um palindromo, desconsiderando os espaços.

Ex:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
"""
frase = str(input('Digite uma frase: ')).strip().upper() #  Tirei espaços antes e depois; coloquei tudo em caixa alta
palavras = frase.split() #  Separei as palavras em uma lista.
junto = ''.join(palavras) #  Retirei os espaços entre palavras e juntei as mesmas.
inverso = junto[::-1] #  Fatiamento
'''inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada NÃO é uma palíndromo!')
