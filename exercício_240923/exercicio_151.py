

# IMC = peso/(altura)² ou IMC = peso/altura*altura
# Peso em kg
# altura em metros

# IMC < 20 - Faixa de Risco = abaixo do peso
# IMC entre 20 e 25 - Faixa de Risco = normal
# IMC acima de 25 até 30 - Faixa de Risco = excesso de peso
# IMC acima de 30 até 35 - Faixa de Risco = obesidade
# IMC acima de 35 - Faixa de Risco = obesidade mórbida

peso = float(input('\nDigite seu peso: '))
altura = float(input('\nDigite sua altura: '))
imc = peso/altura**2 

if (imc < 20):
    print('\nAbaixo do peso!')

elif (imc <= 25):
    print('\nNorma!')

elif (imc <= 30):
    print('\nExcesso de peso!')

elif (imc <= 35):
    print('\nObesidade!')

else:
    print('\nObsesidade mórbida!')

print('\n')
