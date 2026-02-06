# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Primeira segmento: '))
r2 = float(input('Segunda segmento: '))
r3 = float(input('Terceira segmento: '))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('Os segmentos a cima PODEM FORMAR UM TRIÂNGULO!')
else:
    print('Os segmentos a cima NÃO PODEM FORMAR UM TRIÂNGULO')

