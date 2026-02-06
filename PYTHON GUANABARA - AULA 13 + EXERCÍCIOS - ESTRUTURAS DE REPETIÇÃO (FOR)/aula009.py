# fatiamento de strintgs
# aula 009
# 09/01/2025
# Conceitos: fatiamento de strings
# objetivo: mostrar como fatiar strings
# Como fatiar strings?
# Exemplo: 

frase='Curso em video Python'
#      0123456789..........20
print(frase[9]) #v
# o python começa a contar do 0 e não do 1
# o que está entre colchetes é o indice da string que queremos mostrar
# o "v" está na posição 9 da string, pois o 9 dentro dos colchetes significa que queremos mostrar o que está na posição desejada
# Outro exemplo:

frase='Curso em Vídeo Python'
print(frase[9:13]) #Víde
# O que está entre os dois pontos é o intervalo de posições que queremos mostrar
# começando do 9 e indo até o 13, mas o 13 não é mostrado, ou seja, o 13 é excluído
# o python sempre exclui o último número do intervalo.
# Outro exemplo:

frase='Curso em video Python'
print(frase[9:13:2]) #ve
# O que está entre os dois pontos é o intervalo de posições que queremos mostrar
# começando do 9 e indo até o 13, mas 13 não é mostrado, ou seja, o 13 é excluído
# Os dois pontos depois do 13 e o 2 significa que queremos mostrar de 2 em 2 posições
# Outro exemplo:

frase='Curso em video Python'
print(frase[5:]) #em video Python
# O que está entre os colchetes deste exemplo é o intervalo que queremos mostrar
# começando do 5 e indo até o final da string
# os dois pontos sem nada depois dele significa que queremos mostrar até o final da string
# Outro exemplo:

frase='Curso em video Python'
print(frase[:5]) #Curso
# Neste exemplo, os dois pontos sem nada antes dele significa que queremos mostrar do início da string até o 5
# o 5 não é mostrado, ou seja, o 5 é excluido.
# Outro exemplo:

frase='Curso em video Python'
print(frase[9::3]) #VePh
# Neste exemplo, temos o 9 que é o início do intervalo
# os dois pontos sem nada depois do 9 significa que queremos mostrar até o final da string
# O 3 sgnifica que queremos fatiar a frase apartir do 9 pulando de 3 em 3.

# Outra utilização de cadeia de strings é a ANÁLISE:
# é saber algumas insformações sobre ela: - comprimento, qual a letra que começa? ou a letra que termina?
# primeiro método que podemos usar:

# len(frase) - len significa: comprimento.
# Qual o comprimento da frase (quantidade de caracteres)

frase='Curso em Video Python'
# Algumas formas utilizando "count":
# count -  signfica que irá contar quantas letras tem na frase.
# Ex.: 'o' - 3
# Outro exemplo:
frase.count('o', 0 , 13)
# Signica que há uma contagem já com fatiamento:
# do 0 até o 13 (lembrando que o 13 é excluido), irá me mostrar quantas letras 'o' tem na frase

frase='Curso em Video Python'
# Outra analise é o comando "find":
# find - significa encotrar.
frase.find('deo')
# Ex.: 'deo' - esta a partir da posição 11
# Ele irá tentar encotrar quantas vezes essa palavra estará na frase.
# Outra funcionalidade de 'find'
frase.find('Android')
# o programa retornará como (-1) - significa que não existe na string apontada.
# Funcionalidade "in": Permite saber se tem uma palavra na string
# o programa retornará com a resposta: "True" na tela.
# Exemplo:
'curso' in frase

frase='Curso em Video Python'
# Outra funcionalidade é o "replace":
# replace - significa substituir.
frase.replace('Python', 'Android')
# Ele irá substituir a palavra "Python" por " Android"

# Outra Funcionalidade é o "upper":
# upper - significa maiúsculo.
frase.upper()
# Ele irá mostrar a frase em maiúscula na tela e não irá alterar a frase original.

# Outra funcionalidade é o "lower":
# lower - significa minúsculo.
frase.lower()
# Ele irá mostrar a frase em minúscula na tela e não irá alterar a frase original.

# Outra funcionalidade é o "capitalize":
# capitalize - significa capitalizar.
frase.capitalize()
# Ele irá mostrar a frase com a primeira letra em maiúscula e os outras em minúscula.

# Outra funcionalidade é o "title":
# title - siginifica título.
frase.title()
# Ele irá mostrar a frase com a primeira letra de cada palavra em maiúscula.

# Outra funcionalidade é o "strip":
# strip - sgnifica tirar.
frase.strip()
# Ele irá tirar os espcaços inúteis no início e no final da frase.

# Outra Funcionalidade é o "rstrip":
# rstrip - significa tirar da direita.
frase.rstrip()
# Ele irá tirar os espaços inúteis da direita da frase.

# Outra Funcionalidade é o "lstrip":
# lstrip - significa tirar da esquerda.
frase.lstrip()
# Ele irá tirar os espaços inúteis da esquerda da frase.

# Parte de divisão de strings:

# Outra funcionalidade é o "split":
# split - significa dividir.
frase = 'Curso em Video Python'
frase.split()
# Ele irá dividir as palavras da frase em uma lista de palavras separadas, assim como "split" podemos 
# criar um parametro para dividir a frase utilusando os espaços entre as palavras.
# o programa irá numerar as palavras da frase, começando do 0.

# Parte de junção de string:

# Outra funcionalidade é o "join":
# join - significa juntar.
frase = 'Curso em Video Python'
'-'.join(frase)
# Ele irá juntar todas as palavras separadas e colocará "-" este traço.





