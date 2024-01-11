ABCD = str(input())

A, B, C, D = map(int, list(ABCD))

for i in range(1<<3):
    ops = ['-'] * 3
    for j in range(3):
        if i>>j & 1:
            ops[j] = '+'
            
    formula = f'{A}{ops[0]}{B}{ops[1]}{C}{ops[2]}{D}'
    if eval(formula) == 7:
        print(formula + '=7')
        exit()