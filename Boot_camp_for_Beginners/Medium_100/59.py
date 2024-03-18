N = int(input())
p = list(map(int, input().split()))

S = [False] * N

for i in range(1, N+1):
    if i == p[i-1]:
        S[i-1] = True

count = 0
for i in range(N-1):
    if S[i] == True and S[i+1] == True:
        count += 1
        S[i] = False
        S[i+1] = False
    elif S[i] == True and S[i+1] == False:
        count += 1
        S[i] = False
if S[N-2] == False and S[N-1] == True:
    count += 1
    
print(count)