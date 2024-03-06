N = int(input())
A = list(map(int, input().split()))

from collections import Counter

B = Counter(A)


import heapq

C = []


for l, n in B.items():
    if n // 2 == 1:
        heapq.heappush(C, -1*l)
    elif n//2 >= 2:
        heapq.heappush(C, -1*l)
        heapq.heappush(C, -1*l)
        
    else:
        continue

if len(C) >=2:
    num1, num2 = -1*heapq.heappop(C), -1*heapq.heappop(C)
    print(num1*num2)
else:
    print(0)
    