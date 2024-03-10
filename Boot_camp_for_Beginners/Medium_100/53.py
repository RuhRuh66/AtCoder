N = int(input())
A = [0] + list(map(int, input().split()))

total_dist = 0
local_dist_list = []
for i in range(N):
    local_dist = abs(A[i+1]-A[i])
    local_dist_list.append(local_dist)
    total_dist += local_dist

local_dist_list.append(abs(A[N]-A[0]))    
total_dist += abs(A[N]-A[0])

ans = []

for i in range(1, N):
    temp = total_dist -local_dist_list[i-1] - local_dist_list[i] + abs(A[i+1] - A[i-1])
    ans.append(temp)

ans.append(total_dist-local_dist_list[N]-local_dist_list[N-1]+abs(A[N-1]-A[0]))

for j in ans:
    print(j)