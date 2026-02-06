# A Confederação de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:

# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anoS: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

from datetime import datetime
ano_atual = datetime.now().year
print('=+'*20)
print(''' [ Até 9 anos: MIRIM     ]
 [ Até 14 anos: INFANTIL ]
 [ Até 19 anos: JUNIOR   ]
 [ Até 20 anos: SÊNIOR   ]
 [ Acima: MASTER         ]''')
print('=+'*20)

ano = int(input('Que ano você nasceu?  '))
idade = (ano_atual - ano)
if idade <= 9:
    print(f'De acordo com a tabela acima, você tem {idade} anos e pertence a categoria (MIRIM).')
elif idade > 10 and idade < 17:
    print(f'De acordo com a tabela acima, você tem {idade} anos e pertence a categoria (INFANTIL).')
elif idade > 18 and idade < 19:
    print(f'De acordo com a tabela acima, você tem {idade} anos e pertence a categoria (JUNIOR).')
elif idade == 20:
    print(f'De acordo com a tabeça acima, você tem {idade} anos e pertence a categoria (SÊNIOR).')
else:
    print(f'De acordo com a tabela acima, você tem {idade} anos e pertence a categoria (MASTER).')


