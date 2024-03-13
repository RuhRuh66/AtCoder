N, C, K = map(int, input().split())
T = []
for i in range(N):
   temp = int(input())
   T.append(temp)
T.sort()

first_p = T[0]
buses = 1
now_on_board = 1
start_lim = T[0] + K
for i in range(1, N):
    if T[i] <= start_lim and now_on_board < C:
        now_on_board += 1
    else:
        buses += 1
        start_lim = T[i]+K
        now_on_board = 1
        
print(buses)

    