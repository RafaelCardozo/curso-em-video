"""Vigésimo Nono Desafio."""
from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em umnúmero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
computador = randint(0, 5) #Faz o computador "PENSAR"
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pesei no número {} e não no {}!'.format(computador, jogador))
