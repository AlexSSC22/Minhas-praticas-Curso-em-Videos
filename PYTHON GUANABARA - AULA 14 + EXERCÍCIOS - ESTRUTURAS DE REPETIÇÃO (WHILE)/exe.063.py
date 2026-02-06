# Escreva um programa que leia um número N inteiro qualquer e mostre
# na tela os N primeiros elementos de uma Sequência de Fibonacci.

# Ex.:

# 0 > 1 > 2 > 3 > 5 > 8

N = int(input('Digite um número para saber o Fibonacci: '))
a = 0
b = 1
c = 0
while c <= N:
    print(a, end= ' > ')
    c += 1
    a, b = b, a + b
print('FIM')
