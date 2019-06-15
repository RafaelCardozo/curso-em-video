u"""EXERCÍCIO059.

Curso de Python===>Professor Gustavo Guanabara--->ModuloII.

Crie um programa que leia dois valores e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior valor
[4] novos núemros
[5] sair do programa

Sei programa deverá realizar a operção solicitada em cada caso.
"""
from time import sleep
print('=-='*10)
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior valor
    [4] novos valores
    [5] sair do programa''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        somar = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, somar))
    elif opcao == 2:
        multiplicar = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, multiplicar))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-='*10)
    sleep(2)
print('Fim do programa! Volte sempre!')
