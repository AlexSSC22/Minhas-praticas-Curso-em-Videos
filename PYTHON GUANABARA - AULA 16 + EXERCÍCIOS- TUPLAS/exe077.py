# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Laranja', 'Globo', 'Paralelepipedo', 'Argumento', 'Energia', 'Similares',
             'Vitoria', 'Goiania', 'Aprovado', 'Empregado', 'Vida', 'Prosperidade',
             'Parceria', 'Fidelidade', 'Amor', 'Respeito', 'Gloria', 'Novo',
             'Elegante', 'Harmonia', 'Paz', 'Conglomerado', 'Pindamonhangaba', 'Itaquaquecetuba', 'Guarulhos')
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

