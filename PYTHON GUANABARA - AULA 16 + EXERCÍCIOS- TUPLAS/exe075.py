# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em
# uma tupla. No final, mostre: 

# A) Quantas vezes aparece o valor 9.
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os números pares.

# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.

numeros = tuple(int(input(f'Digite o {i+1}° número: ')) for i in range(4))

print(f'\nVocê digitou os valores {numeros}')

# A) Quantas vezes aparece o valor 9
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')

# B) Em que posição foi digitado o primeiro valor 3
if 3 in numeros:
    print(f'O valor 3 apareceu pela primeira vez na {numeros.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado.')

# C) Quais foram os números pares
pares = [n for n in numeros if n % 2 == 0]
if pares:
    print(f'Os valores pares digitados foram: {pares}')
else:
    print('Nenhum valor par foi digitado.')



núm = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm: # Lê-se: se o três estiver na tupla.
    print(f'O valor 3 apareceu na {núm.index(3)+1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')
