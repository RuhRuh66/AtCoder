S = list(input())
S = set(S)

good = [{'N', 'S'}, {'N', 'S', 'E', 'W'}, {'E', 'W'}]

if S in good:
    print('Yes')
else:
    print('No')