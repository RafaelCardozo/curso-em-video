u"""AULA PRÁTICA 16.

Curso em Vídeo - Professor Gustavo Guanabara.
"""
lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
print(lanche)

for comida in lanche:
    print(f'Eu vou comer {comida}.')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}.')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')

print(sorted(lanche))  # coloca em ordem
print(lanche)

print('Comi pra caramba!')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.count(5))
print(c.index(2))

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
# del(pessoa)
print(pessoa)
