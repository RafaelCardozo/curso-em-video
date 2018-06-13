"""Trigésimo Primeiro Desafio."""

viagem = float(input('QUal é distância da sua viagem? '))
print('Você está prestes a começar uma viagem de  {} Km.'.format(viagem))
if viagem <= 200:
    print('A passagem custa R${:.2f}'.format(viagem*0.5))
else:
    print('A passagem custa R${:.2f}'.format(viagem*0.45))
