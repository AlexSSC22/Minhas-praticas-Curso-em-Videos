# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite seu nome: ')).strip()
print(f'Esse nome tem SILVA? {'silva' in nome.lower()}')