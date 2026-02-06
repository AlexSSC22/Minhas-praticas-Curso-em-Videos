# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não cotinuar.
# No final, mostre:

# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantos mulheres tem menos de 20 anos.

print('=+='*30)
print('CADASTRAMENTO PESSOAL')
print('=+='*30)

maior_18 = homens = m_menos_20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = continuar = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

    if idade >= 18:
        maior_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        m_menos_20 += 1

    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]

    if continuar == 'N':
        break

print('=+='*30)
print(f'Total de pessoas maiores de 18: {maior_18}')
print(f'Quantidade de homens cadastrados: {homens}')
print(f'Mulheres com menos de 20 anos: {m_menos_20}')




