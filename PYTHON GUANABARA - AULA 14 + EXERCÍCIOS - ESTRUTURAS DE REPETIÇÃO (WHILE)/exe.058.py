# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acerter, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep
print('Sou seu computador...  pensar em um número de 0 até 10 tente adivinhar... ')
tente = 0
cpu = randint(0,10)
print('Será que você consegue adivinhar?')

jogador = -1
while cpu != jogador:
    jogador = int(input('Digite um número: '))
    tente += 1
    print('processando...')
    sleep(3)
    if cpu == jogador:
        print(f'Você venceu com {tente} tentativas.')
    else:
        print(f'Eu venci com {tente} tentativas')    
print('fim')

# Outro modo de fazer

acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite: '))
    palpites += 1
    if jogador == cpu:
        acertou = True
    else:
        if jogador < cpu:
            print('Mais... Tente mais uma vez.')
        elif jogador > cpu:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')





# Outro modo de fazer: 

cpu = randint(0,10)
tente = 1
jogador = int(input('Digite um número: '))
while jogador != cpu:
    print('Erro! Tente novamente')
    jogador = int(input('Digite um número novamente: '))
    tente += 1
print(f'Parabéns!!! Você acertou com {tente} tentaticas')