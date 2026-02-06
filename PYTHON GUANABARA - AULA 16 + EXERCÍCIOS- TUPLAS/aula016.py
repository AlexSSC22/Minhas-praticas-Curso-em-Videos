lanche = ('Hambúger','Suco','Pizza','Pudim')
# Tuplas são imutáveis
# Ex.:
# lanche[1] = 'Refrigerante'
# Na hora de executar, dará erro.

print(lanche[1])
print(lanche[:2])
print(lanche[1:])
print(lanche[-2:])# o menos conta ao contrário

# Estrura de reptição 'for'

for comida in lanche:
    print(f'Eu vou comer {comida}')


# para mostrar a posição:

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}') # Tem momentos que só se resolve desta estrutura

for pos, comida in enumerate (lanche): # nesta forma para mostrar a posição precisamos colocar duas variáveis
    print(f'Eu vou {comida} na posição {pos}')

print('Comi pra caramba!')

print(sorted(lanche)) # Função de ordenar (Alfabética) - O Python colocará os iténs em colchetes 

# Montar Tuplas com números: 
#Ex.:

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print (c) # Irá juntar os números de "a" e "b"

# Se utilizar o "len", "count"
# Exs.:
print (len(c)) # Irá contar o total dos dois termos mencionado a cima
print (c.count(5)) # Neste caso irá mostrar quantas vezes o "número" ou caractere desejado será mostrado "5", ele irá mostrar 2 vezes
print (c.index(4)) # Aqui o programa irá mostrar em que posição está o número ou caractere, se tiver mais números podemos selecionar onde irá começar
                    # a procura.]
# Ex.:
print(c.index(5, 1)) # Desta forma o contador começará na posição um em diante.

# No Python podemos montar Tuplas com tipos diferentes dentro dele.
#Ex: 

pessoa = ('Alex', 39, 'M', 90.23)
print(pessoa)

