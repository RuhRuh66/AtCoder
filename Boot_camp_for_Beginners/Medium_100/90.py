N, Q = map(int, input().split())

S = input()
Acc = [0] * N
temp = 0
for i in range(1, N):
    if S[i] == 'C' and S[i-1] == 'A':
        temp += 1
        Acc[i] = temp
    else:
        Acc[i] = temp

for j in range(Q):
    x, y = map(int, input().split())
    print(Acc[y-1]-Acc[x-1])