num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)# O insert serve para incluir um elemento na lista. O Exemplo usado foi pra add o 0 na posição 2
num.pop() # o pop serve para remover um elemento da lista. Se colocar um parâmetro 'pop(2)' ele irá eliminar o 0

print(num)
print(f'Essa lista tem {len(num)} elementos.')