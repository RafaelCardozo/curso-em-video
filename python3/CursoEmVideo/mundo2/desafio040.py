"""Desafio 040."""
print('=-='*5)
print('Média do Aluno')
print('=-='*5)
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2) / 2
if média <= 5.0:
    print('Tirando {:.1f} e {:.1f} a média é {:.1f}. O aluno está REPROVADO!'.format(nota1, nota2, média))
elif média <= 5.0 or média <= 6.9:
    print('Tirando {:.1f} e {:.1f} a média é {:.1f}. O aluno está de RECUPERAÇÃO!'.format(nota1, nota2, média))
else:
    print('Tirando {:.1f} e {:.1f} a média é {:.1f}. O aluno está APROVADO!'.format(nota1, nota2, média))
