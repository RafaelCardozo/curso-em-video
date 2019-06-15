u"""DESAFIO093.

Curso em Vídeo - Professor Gustavo Guanabara
Módulo 3 - Variáveis Compostas - Dicionários

Crie um programa que gerencie o aproveitamento de um jogador de futebol. O
programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler
 a quantidade de gols feitos em cada partida. No final, tudo isso será guardado
 em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: ')).strip().title()
tot = int(input(f'Quantas partidas {jogador["nome"]}: '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos goasl na {c}ª partida? ')))
jogador['goals'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
