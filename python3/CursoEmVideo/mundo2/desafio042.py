"""Desafio 42."""
print('-=-' * 8)
print('Analisador de Triângulos')
print('-=-' * 8)
a = float(input('Digite o primeiro seguimento de reta: '))
b = float(input('Digite o segundo seguimento de reta: '))
c = float(input('Digite o terceiro seguimento de reta: '))
if a < b + c and b < a + c and c < a + b:
    print('Os seguinmentos acima PODEM FORMAR triângulo!')
    if a == b == c:
        print('Formam um triângulo EQULÁTERO')
    elif a == b != c or a == c != b or b == c != a:
        print('Formam um triângulo ISÓSCELES')
    else:
        print('Formam um triângulo ESCALENO')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR triângulo!')
