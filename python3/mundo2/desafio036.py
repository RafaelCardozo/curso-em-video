"""Desafio 038."""
print('\033[7;30;41m =-=\033[m'*10)
print('Empresta Fácil - Tenha sua Casa Própria')
print('\033[7;30;41m =-=\033[m'*10)
nome = str(input('Digite o nome do Cliente: ')).strip()
casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Em quantos meses deseja pagar a casa? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print('a pŕestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
