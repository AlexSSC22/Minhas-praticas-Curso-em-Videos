# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço e 
# condições de pagamento:

print("""
[(1) - à vista dinheiro/cheque: 10% de desconto]
[(2) - à vista no cartão: 5% de desconto       ]
[(3) - em até 2x no cartão: preço normal       ]
[(4) - 3x ou mais no cartão: 20% de juros      ]\n""")

preço = float(input('Valor do produto: R$ '))
pagamento = int(input('forma de pagamento: '))
if preço >= 100 and pagamento == 1:
    desconto = preço - (preço * 0.1)
    print(f'À vista: Valor do produto R$ {preço:.2f} desconto de 10%: R$ {desconto:.2f}')
elif preço >= 100 and pagamento == 2:
    desconto = preço - (preço * 0.05)
    print(f'À vista no cartão: Valor do produto R$ {preço:.2f} desconto de 5%: R$ {desconto:.2f} ')
elif preço >= 100 and pagamento == 3:
    parcela = (preço / 2)
    print(f'Em até 2x no cartão: Valor do produto R$ {preço:.2f} parcelado em 2X iguas: R${parcela:.2f}')
elif preço >= 100 and pagamento == 4:
    juros = preço + (preço * 0.2)
    parcela = int(input('Em quantas parcelas deseja: '))
    n_parcelas = (juros / parcela)
    if parcela > 3:
        print(f'Em 3x ou mais no cartão: Valor do produto R$ {preço:.2f} \n acima de 3x com juros de 20%: R$ {n_parcelas} / valor total: R$ {juros:.2f}')
    else:
        print('Erro! Opção inválida, tente novamente.')
else:
    print('Ops!!! Opções invalida, tente novamente.')


