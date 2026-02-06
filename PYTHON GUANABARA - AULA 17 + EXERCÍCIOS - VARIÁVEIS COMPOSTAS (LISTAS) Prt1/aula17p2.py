valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')


valores = list()
for cont in range (0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encotrei o valor {v}!')
print('Cheguei ao final da lista.')

# IMPORTANTE:

# Ex.:
a = [2, 3, 4, 7]
# b = a
# Desta forma "b" esta ligado a lista "a"
# para fazer uma cópia dos valores de "a"
b = a[:]
b[2] = 8
print(f'Lista de A: {a}')
print(f'Lista de B: {b}')

