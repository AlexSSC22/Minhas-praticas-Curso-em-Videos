# Escreva um programa que leia salário de um funcionário e calcule o valor do seu aumento.

# Para salário superior a R$ 1.250,00, calcule um aumento de 10%.

# Para os inferiores ou iguais, o aumento é de 15%.

salário = float(input('Digite seu salário: R$ '))
if salário <= 1250:
    aumento = (salário * 0.15) + salário
else:
    aumento = (salário * 0.1) + salário
print(f'Seu salário de {salário} aumentou para {aumento} ')

