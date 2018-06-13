"""Vigésimo Nono Desafio."""
velocidade = float(input('Digite a velocidade que trafegava: '))
if velocidade >= 80:
    print('Você foi muntado em R${:.2f}'.format((velocidade-80)*7)
else:
    print('Parabéns! Conduz com prudência.')
