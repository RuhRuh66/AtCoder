N = int(input())
from collections import Counter


t = []

for i in range(N):
    temp = input()
    t.append(temp)
    
s = Counter(t)
print(s.most_common())
    

