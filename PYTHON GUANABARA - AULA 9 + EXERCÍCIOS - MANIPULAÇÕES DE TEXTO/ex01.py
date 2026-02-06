# Crie um programa que leia o nome completo de uma pessoa e mostre: 

# o nome com todas as letras maiúsculas.
# O nome com todas minúsculas.
# Quantas letras ao todo (sem consuderar espaços).
# Quantas letras tem o primeiro nome.

nome = str (input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print (f'Seu nome em maiúsculas é: {nome.upper()}.')
print (f'Seu nome em minúsculas é: {nome.lower()}.')
# print (f'Seu nome tem {len(nome.replace(' ',''))} ao todo')
# outro modo de realizar este exercicío:
print (f'Seu nome tem {len(nome) - nome.count(' ')} ao todo.')
print (f'Seu primeiro nome tem {nome.find(' ')} letras.')
