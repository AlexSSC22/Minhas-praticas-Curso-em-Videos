# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
# de acordo com a tabela abaixo:
print('=+=' * 20)
print("""
 [- Abaixo de 18.5: Abaixo o peso ]
 [- Entre 18.5 e 25: Peso ideal   ]
 [- 25 até 30: Sobrepeso          ]
 [- 30 até 40: Obesidade          ]
 [- Acima de 40: Obesidade mórbida]\n""")

print('=+=' * 20)

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = (peso / altura) * altura
if imc < 18.5:
    print(f'Seu IMC é {imc:.2f} - Você está abaixo do peso.')
elif imc > 18.5 and imc < 25:
    print(f'Seu IMC é: {imc:.2f} - Você está no peso ideal.')
elif imc > 25 and imc < 30:
    print(f'Seu IMC é: {imc:.2f} - Você está Sobrepeso.')
elif imc > 30 and imc > 40:
    print(f'Seu IMC é: {imc:.2f} - Você está com Obesidade.')
else:
    print(f'Seu IMC é: {imc:.2f} - Você está com Obesidade Mórbida.')