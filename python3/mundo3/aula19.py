u"""AULA PRÁTICA 019.

Curso em Vídeo - Professor Gustavo Guanabara
Módulo 3 - Variáveis Compostas
Dicionários
"""
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)

estado = dict()
brasiu = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input(' Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasiu:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
