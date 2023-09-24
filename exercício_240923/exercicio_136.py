# até 10 anos - R$ 30,00
# acima de 10 até 29 anos - R$ 60,00
# acima de 29 até 45 anos - R$ 120,00
# acima de 45 até 59 anos - R$ 150,00
# acima de 59 até 65 anos - R$ 250,00
# maior que 65 anos - R$ 400,00

nome = str(input('\nEntre com nome:'))
idade = int(input('\nEntre coma idade:'))

if (idade <= 10):
    print(f'\n{nome} pagará R$ 30.00 reais')

elif (idade <= 29 ):
    print(f'\n{nome} pagará R$ 60.00 reais')

elif (idade <= 45):
    print(f'\n{nome} pagará R$ 120.00 reais')

elif (idade <= 59):
    print(f'\n{nome} pagará R$ 150.00 reais')

elif (idade <= 65):
    print(f'\n{nome} pagará R$ 250.00 reais')

else:
    print(f'\n{nome} pagará R$ 400.00 reais')

print('\n')

    


