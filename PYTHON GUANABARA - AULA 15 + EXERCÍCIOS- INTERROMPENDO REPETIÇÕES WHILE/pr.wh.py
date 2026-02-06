x = 0
s = 0
while True:
    n = int(input('Escreva um número: '))
    if n == 999:
        break
    x += 1
    s += n
print(f'{s} e {x}')