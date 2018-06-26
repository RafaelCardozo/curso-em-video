"""Desafio 43."""
print('-=-'*12)
print('\033[31m I.M.C. - Índice de Massa Corporal\033[m')
print('-=-'*12)
altura = float(input('Qual é a sua altura em metros? '))
peso = float(input('Qual é o seu peso em Kg? '))
imc = peso / altura ** 2
print('Seu I.M.C. é {:.1f}'.format(imc))
if imc < 16:
    print('Magreza Grave! PROCURE UM MÉDICO URGENTE!')
elif 16 <= imc < 17:
    print('Magreza Moderada! PROCURE UM MÉDICO!')
elif 17 <= imc < 18.5:
    print('Magreza Leve! PROCURE UM NUTRICIONISTA!')
elif 18.5 <= imc < 25:
    print('Você está SAUDÁVEL!')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO. CUIDADO!!!')
elif 30 <= imc < 35:
    print('Obesidade de Grau I. Procure um NUTRICIONISTA!')
elif 35 <= imc < 40:
    print('Obesidade de Grau II (severa). Procure um MÉDICO!')
else:
    print('Obesidade de Grau III (morbida). Procure um MÉDICO!!!!')
