# Crei um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maior idade e quantas já são de maiores.

# OBS.: 
# Considerar a maior idade de 21 anos.

nasc_maior = 0
nasc_menor = 0
from datetime import date
ano = date.today().year
for idade in range(1, 8):
    nascimento = int(input(f'{idade}° Ano de nascimento: '))
    data = (ano - nascimento)
    if data <= 21:
        nasc_menor += 1
    else:
        nasc_maior += 1
print(f'Ao todo tivemos {nasc_menor} pessoas menores de idade')
print(f'e também tivemos {nasc_maior} pessoas maiores de idade.')
