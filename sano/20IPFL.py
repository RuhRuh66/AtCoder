N = int(input())
S = list(str(input()))
Q = int(input())

queries = []
for i in range(Q):
    temp = list(map(int, input().split()))
    queries.append(temp)

status = True

for i in queries:
    if i[0] == 1:
        if status == True:
            S[i[1]-1], S[i[2]-1] = S[i[2]-1], S[i[1]-1] 
        else:
            if i[1] <= N:
                i[1] += N
            else:
                i[1] -= N
            if i[2] <= N:
                i[2] += N
            else:
                i[2] -= N
            S[i[1]-1], S[i[2]-1] = S[i[2]-1], S[i[1]-1] 
    else:
        status = not status
        
if status == True:
    print(''.join(S))
else:
    print(''.join(S[N:]+S[:N]))
    
    