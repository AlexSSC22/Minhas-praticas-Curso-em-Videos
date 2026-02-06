# Faça um programa que calcule a soma de todos os números impares que são múltiplos de três e
# que se encontram no intervalo de 1 até 500.

somatório = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        somatório += c
print(f'A somatória dos números impares são: {somatório}')