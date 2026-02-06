# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

# - Se ele ainda vai se alistar no serviço militar
# - Se é hora de se alistar
# - Se já passou do tempo de alistamento.

# Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo.

from datetime import date

ano_atual = date.today().year 
# Neste metodo estamos usando "now" (para import datetime), mas pode ser "today"(para import date) pra definir o tempo atual.
nascimento = int(input('Qual ano que você nasceu? '))
print('Qual a sua sexualidade? (M) ou (F)')
sexo = str(input('Defina seu sexo: ')).strip()
if sexo.upper() == 'M':
    idade = (ano_atual - nascimento)
    print(f'Você completou {idade} anos em {ano_atual}')
    if idade < 18:
        saldo = (18 - idade)
        print(f'Faltam {saldo} anos para você se alistar ')
        ano = (ano_atual + saldo)
        print(f'Seu ano de alistamento será em {ano}')
    elif idade == 18:
        print(f'Já esta na hora de se alistar')
    elif idade > 18:
        # podemos usar "elif" ou "else"
        saldo = (idade - 18)
        print(f'Ops!!! já se passou {saldo} anos da data do seu alistamento.')
        ano = (ano_atual - saldo)
        print(f'Seu ano de alistamento seria em {ano}')
else:
    print('Você não precida se alistar.')


