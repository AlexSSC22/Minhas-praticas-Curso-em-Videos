# Desenvolva um programa que pergunte a distância de uma viagem em Km.

# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,40 para viagens mais longas.

distância = int(input('Qual a disntância da viagem? Km: '))
if distância <= 200:
    valor = (distância * 0.5)
    print(f'Com a distância de {distância} o valor fica R$ {valor:.2f}.')
else:
    valor = (distância * 0.4)
    print(f'Com a distância de {distância} o valor fica R$ {valor:.2f}')
print('BOA VIAGEM!')