# Crei um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência.

# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ('Frango', 9.95,
            'Abobora', 5.63,
            'Abacaxi', 2.5,
            'limão', 1.25,
            'Pão', 2.65,
            'Aguá de coco', 7.75,
            'Televisão', 2999,
            'Camiseta', 45.9)
largura = len('=+=' * 15)
print('=+=' * 15)
print(f'{'LISTAGEM DE PREÇO!':^{largura}}')
print('=+=' * 15)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<35}', end='')
    else:
        print(f'{listagem[pos]:>7.2f}')
