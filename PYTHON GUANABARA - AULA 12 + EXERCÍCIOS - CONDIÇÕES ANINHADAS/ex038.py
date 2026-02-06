# Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
# - O primeiro número é maior
# - O segundo número é maior
# - Não exite valor maior, os dois são iguais.


n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print(f'O número maior é {n1} e o menor é {n2}')
elif n2 > n1:
    print(f'O maior número é {n2} e o menor é {n1}')
else:
    print(f'Não existe valor maior, os dois são iguais. {n1} e {n2}')

