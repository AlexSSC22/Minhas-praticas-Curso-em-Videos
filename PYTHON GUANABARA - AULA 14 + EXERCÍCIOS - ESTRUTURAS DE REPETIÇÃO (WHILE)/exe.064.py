# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só irá parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = 0
c = 0
num = 0

while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        soma += num
        c += 1
print(f'Você digitou {c} números e a soma entre eles foi {soma}.')
