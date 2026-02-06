# Escreva um programa que leia a velocidade de um carro.

# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada KM acima do limite.

velocidade = int(input('Velocidade atingida: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'ATENÇÃO! Você foi ultrpassou o limite da velocidade e foi multado no valor de R$ {multa:.2f}.')
else:
    print('VELOCIDADE OK! Pode seguir. Boa viagem!')