# _*_ coding: utf-8 _*_
lag = float(input('Digite o largura em metros: '))
h = float(input('Digite a altura em metros: '))
a = lag*h
r = 2
t = a/r
print('A área de {}m² necessita de {}l de tinta para ser printada'.format(a, t))
