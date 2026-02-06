# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas aqueles que forem pares. 
# Se o valor digitado for impar, desconsidere-o.


soma = 0
cont = 0
for c in range(1, 7):
    número = int(input(f'Digite o {c}°: '))
    if número % 2 == 0:
        soma = soma + número # ou soma += número
        cont = cont + 1 # ou cont += 1 
        # Detalhe: O "cont" irá contar quantas vezes os números pares estão aparecendo
        # O mesmo acontece com a soma, ela irá somar os números que atenderem a condição posta.
print(f'Você informou {cont} números PARES e a soma foi {soma}.')

        