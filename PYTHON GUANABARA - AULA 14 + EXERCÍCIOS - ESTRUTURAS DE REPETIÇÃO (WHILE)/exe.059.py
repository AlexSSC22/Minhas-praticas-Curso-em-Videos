# Crei um programa que leia dois valores e mostre um menu na tela:

''' 
[1] soma
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
'''
# Seu programa deverá realizar operação solicitada em cada caso.


n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [1] soma
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')

    opção = int(input('>>>>>>>> Escolha a opção desejada:  '))
    if opção == 1:
        soma = (n1 + n2)
        print(f'A soma de {n1} e {n2} é: {soma}')
    elif opção == 2:
        mult = (n1 * n2)
        print(f'A multiplicação de {n1} e {n2} é: {mult}')
    elif opção == 3:
        if n1 > n2:
            print(f'{n1} maior')
        else:
            print(f'{n2} maior')
    elif opção == 4:
        print('Digite os valores novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)    

print('Fim do programa! Volte sempre.')




