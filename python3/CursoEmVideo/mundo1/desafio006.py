u"""Desafio006.

Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
"""
n = int(input('Digite um número inteiro: '))
print('O número digitado foi {}, o número antecessor é {}, o número sucessor é {}'.format(n, (n-1), (n+1)))
