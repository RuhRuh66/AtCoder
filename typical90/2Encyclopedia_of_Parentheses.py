N = int(input())

from itertools import combinations

if N % 2 == 1:
    print('')
    exit()
    

comb = combinations(list(range(N)), N//2)
for bra in comb:
    parentheses = [')'] * N
    for i in bra:
        parentheses[i] = '('
    
    ans = 0
    for j in parentheses:
        if j == '(':
            ans += 1
        else:
            ans -= 1
            if ans < 0:
                break
    if ans == 0:
        print(''.join(parentheses))
        

    
