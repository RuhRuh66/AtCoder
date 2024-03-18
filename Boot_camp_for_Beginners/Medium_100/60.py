N = int(input())

from collections import defaultdict
from itertools import combinations

T = defaultdict(int)

for i in range(N):
    temp = input()
    if temp[0] in ['M', 'A', 'R', 'C', 'H']:
        T[temp[0]] += 1

count = 0
for A, B, C in combinations(T, 3):
    count += T[A]*T[B]*T[C]
    
print(count)
    
    
        
        