u"""AULA020.

CURSO EM VÍDEO - Professor Gustavo Guanabara
Módulo 3 - Funções (Parte1)
"""
# Raciocíno do programa
# a = 4
# b = 5
# s = a + b
# print(s)

# a = 8
# b = 9
# s = a + b
# print(s)

# a = 2
# b = 1
# s = a + b
# print(s)


def soma(a, b):
    s = a + b
    print(s)


# Programa Principal
soma(4, 5)
soma(8, 9)
soma(2, 1)

# Empacotamento de Tuplas


def contador(* núm):
    print(núm)
    for valor in núm:
        print(f'{valor} ', end='')
    print('FIM')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# Empacotamento de Listas


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)
