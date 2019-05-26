u"""DESAFIO077.

Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
 Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
print('-' * 30)
print(f'{"PALAVRAS SEM ACENTOS":^30}')
print('-' * 30)
palavras = (str(input('Digite uma palavra: ')).strip().upper(),
            str(input('Digite uma palavra: ')).strip().upper(),
            str(input('Digite uma palavra: ')).strip().upper(),
            str(input('Digite uma palavra: ')).strip().upper(),
            str(input('Digite uma palavra: ')).strip().upper(),
            str(input('Digite uma palavra: ')).strip().upper(),
            str(input('Digite uma palavra: ')).strip().upper(),
            str(input('Digite uma palavra: ')).strip().upper())
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
