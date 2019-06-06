u"""AULA PRÁTICA017.

Curso em Vídeo - Professor Gustavo Guanabara.
"""
num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
num.insert(2, 0)
print(num)
num.pop(2)
print(num)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos.')

valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...')
for c, v in enumerate(valores):
    print(f'Na posição {c} encomtrei o valor {v}!')
print('Cheguei ao final da lista.')
