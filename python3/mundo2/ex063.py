u"""EXERCÍCIO062.

Curso de Python===>Professor Gustavo Guanabara--->ModuloII.

Melhores o DESAFIO061, perguntando para o usuário se el quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
"""
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
termo = primeiro
count = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while count <= total:
        print('{} ¬'.format(termo), end='')
        termo += razão
        count += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
