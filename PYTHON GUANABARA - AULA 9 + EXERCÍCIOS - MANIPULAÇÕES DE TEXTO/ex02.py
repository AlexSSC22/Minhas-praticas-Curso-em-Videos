# Faça um progragam que leia um número de 0 a 999 e mostre na tela cada um dos diigitos separados.

# Ex.:

# Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

número = int(input('Digite um número: '))
u = número // 1 % 10
d = número // 10 % 10
c = número // 100 % 10
m = número // 1000 % 10
print (f'Analisando o número {número}:')
print (f'Unidade: {u} ')
print (f'Dezena: {d} ')
print (f'Centena: {c} ')
print (f'Milhar: {m} ')