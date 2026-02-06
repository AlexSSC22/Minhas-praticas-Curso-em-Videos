# Escreva um programa que leia um número qualquer e peça para o usuário escolher qual será a base de conversão:

# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal
print('''Escolha uma opção para conversão desejada:
      - 1: binario
      - 2: octal
      - 3: hexadecimal''')
número = int(input('Digite um número: '))
opção = int(input('Escolha uma das opções de conversão: '))
if opção == 1:
    print(f'O número {número} na opção {opção} é {bin(número)[2:]} em binário')
elif opção == 2:
    print(f'O número {número} na opção {opção} é {oct(número)[2:]} em octal')
elif opção == 3:
    print(f'O número {número} na opção {opção} é {hex(número)[2:]} em hexadecimal')
else:
    print('Opção invalida, tente novamente.')
