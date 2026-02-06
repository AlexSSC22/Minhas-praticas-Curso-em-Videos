# Exemplo prático de condição simples:

nome = str(input('Qual é seu nome? '))
if nome == 'Alex':
    print('que nome lindo você tem!')
# Exemplo de condição composta:
else:
    print('Seu nome é tão normal!')
print(f'Bom dia {nome}!')

# Outro programa com condição composta:

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi {m:.1f}')
if m >= 6.0:
    print('Sua média foi boa! PARABÊNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')