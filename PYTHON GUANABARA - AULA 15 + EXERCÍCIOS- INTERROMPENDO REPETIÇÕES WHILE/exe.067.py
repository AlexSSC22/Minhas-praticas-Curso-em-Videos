# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.




while True:
    tab = int(input('Descubra a tabuada do número: '))
    if tab < 0:
        break
    c = 1
    while c <= 10:
        print(f'{c} x {tab} = {c * tab}')
        c += 1
print('PROGRAMA ENCERRADO. Volte sempre!')

