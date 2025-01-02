N, M = map(int, input().split())
A = list(map(int, input().split()))

B = [-i for i in A]

from heapq import heapify, heappop, heappush

heapify(B)

for i in range(M):
    c = heappop(B)
    d = -(-c//2)
    heappush(B, d)
    
print(-sum(B))Sp = input()
T = input()

s = len(Sp)
t = len(T)

for i in range(s-t, -1, -1):
    target = Sp[i:i+t]
    flag = True
    for j in range(t):
        if target[j] == T[j]:
            continue
        elif target[j] == '?':
            continue
        else:
            flag = False
            break
    if flag == True:
        pre_ans = Sp[:i] + T + Sp[i+t:]
        ans = pre_ans.replace('?', 'a')
        print(ans)
        exit()
        
print('UNRESTORABLE')
