N = int(input())
S = input()

putFirst = 0
putLast = 0

now_count = 0

for i in range(N):
    if S[i] == '(':
        now_count += 1
    elif S[i] == ')':
        now_count -= 1
        
        if now_count == -1:
            putFirst += 1
            now_count = 0
putLast = now_count
ans = '(' * putFirst + S + ')' * putLast

print(ans)
        
