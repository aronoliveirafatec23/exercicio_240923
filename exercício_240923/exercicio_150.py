# o seno do ângulo, se o ângulo pertencer a um quadrante par;
# o co-seno do Ângulo, se o ângulo pertencer a um quadrante ímpar.

import math as m

angulo = float(input('\nDigite ângulo em graus:'))
rang = (angulo*3.14)/180

if (rang > 3.14/2 and rang <= 3.14) or (rang > 3 * 3.14/2 and rang <= 2 * 3.14):
    print(f'\nseno = sen{rang}')

else:
    print(f'\nco-seno = cos{rang}')

print('\n')
