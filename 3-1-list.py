# 3.1. Įvedamas masyvas. Parašykite programą, kuri apskaičiuotų masyvo teigiamų lyginių elementų, nelygių nuliui, sandaugą. 

import random
list = random.sample(range(0, 101), 10)
print(f'Naudojamas sarasas: {list}')
sandauga = 1

for i in list:
    if i % 2 == 0 and i != 0:
        print(f'{i} yra lyginis ir bus naudojamas sandaugai')
        sandauga *= i
print(f'Saraso elementu andauga: {sandauga}')