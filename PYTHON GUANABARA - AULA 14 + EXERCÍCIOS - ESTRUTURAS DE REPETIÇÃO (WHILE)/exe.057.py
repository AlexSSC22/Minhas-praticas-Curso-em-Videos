# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter o valor correto.

s = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
while s != 'F' and s != 'M': # Ou desta forma - while s not in 'MmFf': (neste exemplo a condição não irá acontecer enquanto o sexo não for definido.)
    print(f'{s} Não é um opção valida, digite novamente.')
    s = str(input('Digite o sexo novamente [M/F]: ')).upper().strip()[0]
print(f' Sexo {s} cadastrado com sucesso')

    


