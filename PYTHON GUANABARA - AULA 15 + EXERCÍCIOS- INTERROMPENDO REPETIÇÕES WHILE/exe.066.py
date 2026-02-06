#  Crie um programa que leia vários números inteiros pelo teclado. o programa só
# vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles

# (Desconsiderando o flag).

c = s = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    s += num # Se é colocado essa conta antes da condição é somado o valor "999"
    c += 1
print(f'Você digitou {c} números e a soma deles é {s}')  


    

