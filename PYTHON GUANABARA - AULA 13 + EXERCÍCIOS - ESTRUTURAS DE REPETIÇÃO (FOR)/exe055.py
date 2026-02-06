# Faça um programa que leia o peso de 5 pessoas.
# No final, mostre qual foi o maior e o menor peso lido.

maior = 0
menor = 0
for p in range (1, 6):
    peso = float(input(f'{p}° medida de peso: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'Peso maior lido: {maior}KG')
print(f'Peso menor lido: {menor}KG')