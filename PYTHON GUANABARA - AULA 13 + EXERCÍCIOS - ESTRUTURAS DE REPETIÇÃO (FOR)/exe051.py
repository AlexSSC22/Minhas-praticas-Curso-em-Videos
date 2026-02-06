# Desevenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Primeiro termo: '))
razão = int(input('Digite a razão: '))
décimo = primeiro + (20 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print(f'{c}', end= ' > ')
print('ACABOU')


