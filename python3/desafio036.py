"""Trigésimo Sexto Desafio."""
print('-=-' * 15)
print('Analisador de Triângulos')
print('-=-' * 15)
a = float(input('Digite o primeiro seguimento de reta: '))
b = float(input('Digite o segundo seguimento de reta: '))
c = float(input('Digite o terceiro seguimento de reta: '))
if a < b + c and b < a + c and c < a + b:
    print('Os seguinmentos acima PODEM FORMAR triângulo!')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR triângulo!')
