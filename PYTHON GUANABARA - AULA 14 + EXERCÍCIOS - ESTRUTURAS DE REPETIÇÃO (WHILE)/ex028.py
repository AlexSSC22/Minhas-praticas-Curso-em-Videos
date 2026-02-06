# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 
# e peça para o usuario tentar descobrir qual foi o número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
print('+-=' * 20)
print('Vou pensar em um número de 0 a 5, tente adivinhar...')
print('+-=' * 20)
cpu = randint(0,5)
jogador = int(input('Digite seu número: '))
print('processando...')
sleep(3)
if jogador <= 5 and jogador == cpu:
    print(f'GANHOOOUU!!! Você me venceu!!! Meu número foi {cpu} e o seu foi {jogador}')
else:
    print(f'OPAAA!!! EU VENCI!!! O número que você jogou foi {jogador} e o meu foi {cpu}')



