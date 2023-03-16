H, W = map(int, input().split())
A = [[] for i in range(H)]
for j in range(W):
    temp = list(map(int, input().split()))
    A[j] = temp
    
got_number_list  = []
start = [0, 0]


from collections import deque
s = deque()
s.append(start)
count = 0
ans = 0
while len(s) > 0:
    i, j = s.popleft()
    now_point = A[i][j]
    if now_point not in got_number_list:
        got_number_list.append(now_point)
        count += 1
        if i+1 <= H-1:
            next_point = [i+1, j]
            s.append(next_point)
        if j+1 <= W-1:
            next_point = [i, j+1]
            s.append(next_point)

    else:
        continue
    
    if count == H+W-2:
        ans += 1
print(ans)
    
    

