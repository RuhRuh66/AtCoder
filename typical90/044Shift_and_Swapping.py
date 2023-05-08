N, Q = map(int, input().split())
A = list(map(int, input().split()))
queries = []
for i in range(Q):
    temp = list(map(int, input().split()))
    queries.append(temp)
    
T2_count = 0

for i in queries:
    if i[0] == 1:

        x = i[1] - T2_count 
        y = i[2] - T2_count
        while x <0:
            x += N
        while y <0:
            y += N
        A[x-1], A[y-1] = A[y-1], A[x-1]
        
    elif i[0] == 2:
        T2_count += 1
        
    else:
        print(A[i[1]-T2_count-1])
        
    
        