N, K = map(int, input().split())
A =list(map(int, input().split()))

from collections import defaultdict
S = defaultdict(int)

for i in range(N):
    S[A[i]] += 1    


S = sorted(S.items(), key= lambda x:x[1])

if len(S) <= K:
    print(0)
    exit()
else:
    count = 0
    for i in range(len(S)-K):
        count += S[i][1]
        
print(count)
        