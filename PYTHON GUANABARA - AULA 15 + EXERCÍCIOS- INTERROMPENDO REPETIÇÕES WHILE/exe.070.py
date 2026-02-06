# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final, mostre:

# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.



print('=+=' * 30)
print('PERIFICANDO PRODUTOS')
print('=+=' * 30)

tg = qt_produtos = menor_preço = 0
produt_barato = ' '


while True:
    produto = str(input('Digite o nome do produto: '))
    v_produto = float(input('Valor do produto  R$: '))

    tg += v_produto

    if v_produto >= 1000:
        qt_produtos += 1
    if menor_preço == 0 or v_produto < menor_preço:
        menor_preço = v_produto
        produt_barato = produto
    
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('=+=' * 30)
print(f'Total gasto: R$ {tg:.2f}')
print(f'Quantidade de produtos acima de R$1000 : {qt_produtos}')
print(f'Produto mais barato: {produt_barato} R$ {menor_preço:.2f}')
    

