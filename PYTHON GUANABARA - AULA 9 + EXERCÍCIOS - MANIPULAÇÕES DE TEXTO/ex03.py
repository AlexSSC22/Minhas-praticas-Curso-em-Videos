# Crie um progama que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".


cidade = str(input('Digite a cidade: ')).strip()
print(f'Essa cidade tem SANTO no começo? {cidade[:5].upper() == 'SANTO'}')