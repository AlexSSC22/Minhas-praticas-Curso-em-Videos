# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele irá pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou o empréstimo será negado.


imóvel = float(input('Qual o valor da casa? R$ '))
salário = float(input('Qual é o seu salário? R$ '))
anos = int(input('Em quantos anos irá parcelar? '))
tempo = (anos * 12)
p = (imóvel / tempo)
if p <= (salário * 0.3):
    print(f'EMPRÉSTIMO APROVADO! No prazo de {anos} total de {tempo} meses, o valor prestação R$ {p:.2f}.', end='') 
    print('Está dentro dos 30% do seu salário')
else:
    s = (salário * 0.3)
    print(f'EMPRÉSTIMO NEGADO! Valor compromete os 30% do seu salário R${s:.2f}, valor da prestação R$ {p:.2f}')