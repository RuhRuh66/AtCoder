N = int(input())
A = list(map(int, input().split()))

nums = [0] * 100001

for num in A:
    nums[num] += 1
    
from math import comb

ans = 0    
for j in range(1, 50000):
    ans += (nums[j]*nums[100000-j])
ans += comb(nums[50000], 2)
    
print(ans)