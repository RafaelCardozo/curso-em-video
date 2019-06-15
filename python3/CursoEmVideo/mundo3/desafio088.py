u"""DESAFIO085.

Curso de Python===>Professor Gustavo Guanabara--->ModuloII.

Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa
vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('      JOGA NA MEGA SENA       ')
print('-' * 30)
quant = int(input('Quantos jogos você quer gerar?'))
tot = 1
while tot <= quant:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'-=' * 3, f' SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
