H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]

moves = [(0, 1), (1, 0)]

ans = 0
from itertools import combinations
for x in combinations(range(H+W-2), H-1):
    route = [1 if i in x else 0 for i in range(H+W-2)]
    
    nums = set()
    nx, ny = 0, 0
    nums.add(A[nx][ny])
    for j in route:
        if j == 0:
            nx += 0
            ny += 1
   
        else:
            nx += 1
            ny += 0
            
        if A[nx][ny] not in nums:
            nums.add(A[nx][ny])
        else:
            continue    
            
    if len(nums) == (H+W-1):
        ans += 1

print(ans)