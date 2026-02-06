# Faça um progama que leia uma frase pelo teclado e mostra:

# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.


frase = str (input('Escreva uma frase: ')).upper().strip()
print(f'Está frase tem {frase.count('A')} letras "A".')
print(f'A letra "A" aparece pela primeira vez na posição {frase.find('A')+1}.')
print(f'A letra "A" aparece pela última vez na posição {frase.rfind('A')+1}')