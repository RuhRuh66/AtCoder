N = int(input())
A = []
for i in range(N):
    temp = list(map(int,input().split()))
    A.append(temp)

max_z = -10**10
min_z = 10**10

max_w= -10**10
min_w = 10**10

for i in A:
    z = i[0] + i[1]
    w = i[0] - i[1]
    
    max_z = max(max_z, z)
    min_z = min(min_z, z)
    max_w = max(max_w, w)
    min_w = min(min_w, w)

print(max(abs(max_z-min_z), abs(max_w-min_w)))