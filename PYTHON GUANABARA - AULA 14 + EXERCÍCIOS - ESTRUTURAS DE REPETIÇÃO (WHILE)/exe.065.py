# Crie um programa que leia vários números inteiros pelo teclado.
# no final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
# O programa deve perguntar ao usuário se ele quer ou não continuar digitar valores. 

resp = 'S'
media = soma = quant = menor = maior = 0

while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    
media = soma / quant
print(f'Você digitou {quant} e a média foi {media}')
print(f'O maior número é {maior} e o menor é {menor}')
print('Fim')

