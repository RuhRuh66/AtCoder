S = input()

A = S.count('a')
B = S.count('b')
C = S.count('c')

if  A == B == C:
    ans = 'YES'
elif A == B == C-1 or A-1 == B == C or A == B-1 == C:
    ans = 'YES'
elif A == B == C+1 or A+1 == B == C or A == B+1 == C:
    ans = 'YES'
else:
    ans = 'NO'
    
print(ans)