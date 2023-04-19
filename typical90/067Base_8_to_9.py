N, K = map(int, input().split())

if N == 0:
    print(0)
    exit()

def num_n_to_10(num_n, n):
    num_n = str(num_n)
    ans = 0
    d = 0
    num_n = list(num_n)
    num_n.reverse()
   
    for i in range(len(num_n)):
        ans += int(num_n[i]) * (n**d)
        d += 1
        
    return ans
        
        
def num_10_to_n(num_10, n):
    ans = []
    while num_10 > 0:
        res = num_10 % n
        ans.append(str(res))
        num_10 = int(num_10//n)
  
        
        
    ans = ''.join(ans[::-1])
    return ans


import re

for i in range(K):
    N = num_n_to_10(N, 8)
    N = num_10_to_n(N, 9)
    N = int(re.sub(r'8', r'5', N))

print(N)