u"""Desafio072.

Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por
 extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-la por
 extenso.
"""
cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenovo', 'vinte')
while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
        break
    print('Tende novamente. ', end='')
print(f'Você digitou o número {cont[núm]}')
