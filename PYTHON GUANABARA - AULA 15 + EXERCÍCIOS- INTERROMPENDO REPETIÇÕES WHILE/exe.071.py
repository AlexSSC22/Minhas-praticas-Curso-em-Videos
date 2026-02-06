# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o
# programa vai informar quantas cédulas de cada valor serão entregues.

# OBS: Considerando que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


largura = len('=+=' * 30)  # Conta quantos caracteres tem a moldura
print('=+=' * 30)
print(f' {"BEM VINDO AO BANCO LEQUINHO!":^{largura}}')
print('=+=' * 30)


valor = int(input('Digite o valor para saque: R$ '))
céd = 50
totcéd = 0
while True:
    if valor >= céd:
        valor -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
            
        elif céd == 20:
            céd = 10
            
        elif céd == 10:
            céd = 1
        totcéd = 0
        if valor == 0:
            break



