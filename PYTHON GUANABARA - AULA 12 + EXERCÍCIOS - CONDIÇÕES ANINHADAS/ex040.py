# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando um mensagem no final, de acordo com a média atingida:

# - Média abaixo de 5.0: REPROVADO:
# - Média entre 5.0 e 6.9:RECUPRAÇÃO
# - Média 7.0 ou superior: APROVADO

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
media = (n1 + n2 + n3 + n4)/4
if media <= 5:
    print(f'Com as notas {n1}, {n2}, {n3} e {n4}, sua média foi {media:.2f}. REPROVADO!')
elif media > 5 and media < 6.9:
    print(f'Com as notas {n1}, {n2}, {n3} e {n4}, sua média foi {media:.2f}. RECUPERAÇÃO!')
else:
    print(f'Com as notas {n1}, {n2}, {n3} e {n4}, sua média foi {media:.2f}. APROVADO!')

