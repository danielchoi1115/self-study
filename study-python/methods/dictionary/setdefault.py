import random

# Two line typical coding
d = {}
for k in ['a', 'b', 'c', 'd', 'a']:
    if k in d:
        d[k].append(random.randint(0,10))
    else:
        d[k] = [random.randint(0,10)]
print(d)


# smarter coding using One line setdefault function
d = {}
for k in ['a', 'b', 'c', 'd', 'a']:
    d.setdefault(k, []).append(random.randint(0,10))
print(d)