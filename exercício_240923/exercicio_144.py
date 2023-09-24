# saldo de 0 a 500 reais - nenhum crédito
# saldo de 501 a 1000 reais - 30% do valor do saldo médio
# saldo de 1001 a 3000 reais - 40% do valor do saldo médio
# saldo acima de 3001 reais - 50% do valor do saldo médio

saldomedio = float(input('\nDigite o saldo médio:'))

if (saldomedio <= 500):
    print(f'\nComo seu saldo era de {saldomedio}, você não terá nenhum crédito.')

elif (saldomedio <= 1000):
    credito = saldomedio * 0.3
    print(f'\nComo seu saldo era de {saldomedio}, seu crédito será de {credito:.2f} em reais.')

elif (saldomedio <= 3000):
    credito = saldomedio * 0.4
    print(f'\nComo seu saldo era de {saldomedio}, seu crédito será de {credito:.2f} em reais.')

elif (saldomedio >= 3001):
    credito = saldomedio * 0.5
    print(f'\nComo seu saldo era de {saldomedio}, seu crédito será de {credito:.3f} em reais.')

print('\n')
    

