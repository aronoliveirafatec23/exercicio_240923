# destino 1 = Região Norte - R$ 500,00 (ida) - R$ 900,00 (ida e volta)
# destino 2 = Região Nordeste - R$ 350,00 (ida) - R$ 650,00 (ida e volta)
# destino 3 = Região Centro-Oeste - R$ 350,00 (ida) - 600,00 (ida e volta)
# destino 4 = Região Sul - R$ 300,00 (ida) - 550,00 (ida e volta)

op = int(input('\nDigite 1 - Região Norte \ 2 - Região Nordeste \ 3 - Região Centro-Oeste \ 4 - Região Sul -  '))
iv = int(input('\nDigite 1 - IDA \ 2 - IDA e VOLTA -  '))

if (op == 1):
    if (iv == 1):
        print('\nOvalor da passagem de IDA para a Região Norte é de R$ 500.00 reais')
    elif (iv == 2):
        print('\nO valor da passgaem de IDA e VOLTA para a Região Norte é de R$ 950.00 reais')
    
elif (op == 2):
    if (iv == 1):
        print(f'\nO valor da passagem de IDA para a Região Nordeste é de R$ 350.00 reais')
    elif (iv == 2):
        print(f'\nO valor da passagem de IDA e VOLTA para a Região Nordeste é de R$ 650.00 reais') 

elif (op == 3):
    if (iv == 1):
        print(f'\nO valor da passagem de IDA para a Região Centro-Oeste é de R$ 350.00 reais')
    elif (iv == 2):
        print(f'\nO valor da passagem de IDA e VOLTA para a Região Centro-Oeste é de R$ 600.00 reais')   

elif (op == 4):
    if (iv == 1):
        print(f'\nO valor da passagem de IDA para a Região Sul é de R$ 300.00 reais')
    elif (iv == 2):
        print(f'\nO valor da passagem de IDA e VOLTA para a Região Sul é de R$ 550.00 reais')   

else:
    print('\nOpção Inexistente!')

print('\n')





