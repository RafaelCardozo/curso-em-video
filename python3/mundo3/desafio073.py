u"""EXERCÍCIO073.

Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
 Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados;
B) Os últimos 4 colocados.
C) Uma lista com os times em ordem alfabética;
D) Em que posição na tabela está o time da Chapecoense.
"""
times = ('Palmeiras', 'Atlético Mineiro', 'São Paulo', 'Santos',
         'Internacional', 'Botafogo', 'Corinthians', 'Flamengo',
         'Atlético Paranaense', 'Bahia', 'Atlético Goianiense', 'Fortaleza',
         'Atlético do Ceará', 'Fluminense', 'Cruzeiro', 'Chapecoense', 'Avaí',
         'Atletico Santa Cruz', 'Grêmio', 'Vasco')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os cinco primeiros são {times[:5]}')
print('-=' * 15)
print(f'Os quatro últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'-=' * 15)
print(f'O Cahapecoense está na {times.index("Chapecoense")+1}ª posição')
