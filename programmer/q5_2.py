import itertools

operators = ['', '+', '-']
for o in itertools.product(operators, repeat=8):
    f = ''
    for n, op in itertools.zip_longest(range(9), o, fillvalue=''):
        f += (str(n + 1)) + op
    if eval(f) == 100:
        print(f)