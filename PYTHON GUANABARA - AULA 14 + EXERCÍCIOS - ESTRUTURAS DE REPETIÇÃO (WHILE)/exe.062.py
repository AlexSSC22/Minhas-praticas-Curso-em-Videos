# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disse que quer mostrar O termos.

primeiro = int(input('Primeiro termo: '))
razão = int(input('Digite a razão: '))
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(primeiro, end=' > ')
        primeiro += razão
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? [press 0 para parar]: '))
print(f'Progressão finalizada com {total} termos mostrados. ')



