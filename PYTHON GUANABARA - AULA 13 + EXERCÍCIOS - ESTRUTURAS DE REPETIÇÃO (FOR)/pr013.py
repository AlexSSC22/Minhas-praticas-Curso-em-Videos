# Se desejar escrever o exeplo a seguir em varias quantidades.

# Exeplo:
#print('oi')
#print('oi')
#print('oi')
#print('oi')
#print('oi')
#print('oi')
# Aqui tempos 6x o "OI"
# Basta fazer desta forma

for c in range(1, 6): # Obs.: Dentro do parenteses temos as divisões das contagens separados por "virgula"(,). Isso 
    # Significa que 
# No lugar de "c" pode se usar qualquer outra variável.
# Detalhe: ele contará de 1 até 5, o ultimo ele não conta.
    print('Oi')
print('FIM')

# Obs.: Se no lugar de "oi" colocar "c".
# o programa contara de 1 até 5
# Exemplo:
for c in range (1, 6):
    print(c)
print('FIM')

# Se desejar uma contagem de 6 até 0 (invertido):
# Exemplo: 
for c in range(6, 0, -1): # O número "-1" é a 'INTERAÇÃO'. Onde o programa entede que onde começa 6 à 0 ele irá subtraindo "-1"
    print(c)
print('FIM')

# Outro tipo de laço seria:
for c in range(0, 7, 2): # Aqui o programa contará de 0 à 6 pulando de 2 em 2.
    print(c)
print('FIM')

# Partindo do mesmo princípio, temos:
n = int(input('Digite um número: '))
for c in range( 0, n+1): # Neste caso ele fará contagem de acordo com o número digitado. A soma do "n+1" é apenas para chegar ao número Digitado
    print(c)
print('FIM')

# Outro Exemplo:
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p): # Aqui O programa começa no "INÌCIO", chegando até o "FIM + 1" e pulando de "PASSO em PASSO".
    print(c)
print('FIM')


# Outro exemplo de for:
for c in range(0, 3 ):
    n = int(input('Digite um valor: '))  # Este comando só esta lendo apenas uma vez, mas será execultado a quantidade que for inserido no "for".
print('FIM')

# Caso queira somar todos esses valores, ficaria assim o programa:
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos esses valores fica {s}.')








