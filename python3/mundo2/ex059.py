u"""EXERCÍCIO058.

Curso de Python===>Professor Gustavo Guanabara--->ModuloII.

Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jopgador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""

from random import randint
from time import sleep
computador = randint(0, 10)
print('-=-'*21)
print('Sou seu computador')
print('.')
sleep(1)
print('..')
sleep(1)
print('...')
sleep(1)
print('Acabei de pensar em números entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
print('-=-'*21)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Em que número pensei? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
