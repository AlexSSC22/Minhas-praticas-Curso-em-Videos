# desenvolva um programa que leia o nome, idade e o sexo de 4 pessoas. No final do programa, mostre:

# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

somaidade = médiaidade = h_m_v = totmulher20 = 0
nomevelho = ''
from datetime import date
ano = date.today().year
for p in range (1, 5):
    print(f'----- {p}° PESSOA -----')
    nome = str(input(' Nome: ')).strip()
    sexo = str(input('Sexo (F)/(M): ')).strip()
    nascimento = int(input('Ano de nascimento: '))
    c_idade = (ano - nascimento)
    somaidade += c_idade
    if p == 1 and sexo in 'Mm':
        h_m_v = c_idade
        nomevelho = nome
    if sexo in 'Mm' and c_idade > h_m_v:
        h_m_v = c_idade
        nomevelho = nome
    if sexo in 'Ff' and c_idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print(f'A média de idade do grupo é: {médiaidade} anos')
print(f'O homem mais velho tem {h_m_v} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')