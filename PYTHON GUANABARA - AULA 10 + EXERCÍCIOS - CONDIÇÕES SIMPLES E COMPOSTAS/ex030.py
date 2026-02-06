# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

número = int(input('Digite um número: '))
n = número % 2
if n == 0:
    print(f'Este número {número} é par.')
else:
    print(f'Este número {número} é impar')

