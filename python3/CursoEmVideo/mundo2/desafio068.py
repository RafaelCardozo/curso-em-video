u"""EXERCÍCIO066.

Curso de Python===>Professor Gustavo Guanabara--->ModuloII.

Crie um programa que leia vários números inteiros pelo teclado. O progrma só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a some entre eles (desconsiderando o flag).
"""
s = cont = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'A soma dos {cont} valores foi {s}!')
