u"""DESAFIO082.

Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares
 e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""
lista = list()
ímpares = list()
pares = list()
while True:
    lista = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        ímpares.append(v)
print('-=' * 30)
print(f'A Lista completa é {lista}')
print(f'A Lista de pares é {pares}')
print(f'A Lista de ímpares é {ímpares}')
