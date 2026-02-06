# Faça um programa que jogue par ou impar com o computados.
# O jogo só será interrompido quando o jogador PEDER, mostrando o total de 
# vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
v = 0

print('=+='*30)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('=+='*30)

while True:
    jogador = int(input('Digite um valor: '))
    cpu = randint(0, 10)
    total = jogador + cpu

    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Escolha PAR ou ÍMPAR [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {cpu} e deu {total} ', end= ' ')
    print ('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if escolha == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')


