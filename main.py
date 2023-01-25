import random

b = []
while True:
    x = random.randint(0,5)
    if x not in b:
        b.append(x)
        print(x, 'add', b)
    else:
        print(x, 'skip', b)
    if len(b) == 6:
        break