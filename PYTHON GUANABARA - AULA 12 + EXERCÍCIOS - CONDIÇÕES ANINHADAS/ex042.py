# Refaça o DESAFIO 035 dos triângulos acrescentando o recurso de mostrar que tipo de triângulo será formado:

# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escalelno: todos os lados diferentes

print('_+_'*20)
print('ANALISANDO TRIÂNGULOS')
print('_+_'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('OS segmentos acima podem formar um triângulo.')
    if r1 == r3 == r2:
        print('Este triângulo é: EQUILÁTERO.')
    elif r1 == r2 or r2 == r1 or r3 == r1:
        print('Este triângulo é: ISÓSCELES.')
    elif r1 != r2 != r3:
        print('Este triângulo é: ESCALENO.')
else:
    print('Os segmentos acima não podem formar um triângulo.')