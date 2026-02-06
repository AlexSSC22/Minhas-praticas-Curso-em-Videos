# Crei uma tupla preenchida com os 20 primeiros colocados da tabela do
# Campeonato Brasileiro, na ordem de colocação. Depois mostre:

# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.

posição = ('Flamengo','Palmeiras','Cruzeiro','Bahia','Botafogo','Mirassol','São Paulo',
           'Fluminense','Bragantino','Ceará SC','Atlético-MG','Internacional','Grêmio',
           'Corinthians','Santos','Vasco da Gama','EC Vitória','Juventudo','Fortaleza',
           'Sport Recife')
print('***' * 30)
print(f'Os cincos primeiros colocados são: {posição [:5]}')
print('***' * 30)
print(f'Os quatros últimos colocados são: {posição [-4:]}')
print('***' * 30)
print(f'Os Times em ordem alfabética: {sorted(posição)}')
print('***' * 30)
print(f'O time do São Paulo está na {posição.index('São Paulo')+1}° posição')

