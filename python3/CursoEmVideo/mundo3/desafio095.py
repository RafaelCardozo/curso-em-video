u"""DESAFIO095.

Curso em Vídeo - Professor Gustavo Guanabara
Módulo 3 - Variáveis Compostas - Dicionários

Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um
 sistema de visualização de detalhes do aproveitamento de cada jogador.
"""
jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: ')).strip().title()
    tot = int(input(f'Quantas partidas {jogador["nome"]}: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos goals na {c + 1}ª partida? ')))
    jogador['goals'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Resposta apenas S ou N')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostra dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f'    LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['goals']):
            print(f'    No jogo {i + 1} fez {g} goals.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
