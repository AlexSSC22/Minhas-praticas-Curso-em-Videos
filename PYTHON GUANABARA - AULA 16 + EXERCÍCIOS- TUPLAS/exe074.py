# Crie um programa que vai gerar cinco números aleatórios e colocar em um tupla.

# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão no tupla.

from random import randint

núm = (randint(1, 10),randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Números sorteados {núm}')
print(f'Maior número {max(núm)}')
print(f'Menor número {min(núm)}')


    