# f(x) = 5x+3/raiz(x²-16)

import math as m

x = float(input('\nDigite o valor de x: '))

if (x > 4 or x < (-4)):
    fx = (5 * x + 3) / m.sqrt(x**2 - 16)
    print(f'\nf(x) = {fx}')

else:
    print('\nNÃO PODE ER FEITA')
print('\n')
