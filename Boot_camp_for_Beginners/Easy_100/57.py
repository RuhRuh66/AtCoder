A, B = map(int, input().split())
from math import floor

for i in range(1, 10000):
    if int(0.08*i) == A and int(0.10*i) == B:
        print(i)
        exit()
        
print(-1)