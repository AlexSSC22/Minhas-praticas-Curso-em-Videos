# Faça um programa que leia um número qualquer e mostre o seu fatorial.

# Ex.:
# 5! = 5x4x3x2x1 = 120

n1 = int(input('Digite um número para calcular seu Fatorial: '))
c = n1
f = 1
print(f'Calculando {n1}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end= '')
    f*=c
    c-=1
print(f'{f}')


# Outra forma:
from math import factorial
n = int(input('Digite um número para cacular seu fatorial: '))
f = factorial(n)
print(f'Fatorial de {n} é: {f}')


# Outro modo utilizando o for: 

n = int(input('Digite um número para calcular o fatorial: '))
f = 1
for c in range(n, 0, -1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end = '')
    f*=c
print(f'{f}')


