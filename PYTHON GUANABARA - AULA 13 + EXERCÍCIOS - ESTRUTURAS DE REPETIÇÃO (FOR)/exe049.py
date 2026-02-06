# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um "laço for".

print('===' * 10 ,'TABUADA', '===' * 10)

número = int(input('Digite o número da tabuada desejada: '))
print(f'A tabuada de {número} é:')
for c in range(0,11):
    print(f'{número} X {c} = {c * número}')



