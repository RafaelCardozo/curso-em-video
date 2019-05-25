u"""EXERCÍCIO061.

Curso de Python===>Professor Gustavo Guanabara--->ModuloII.

Refaça o DESAFIO051, lendo o primerio termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
termo = primeiro
count = 1
while count <= 10:
    print('{} ¬'.format(termo), end='')
    termo += razão
    count += 1
print('FIM')
