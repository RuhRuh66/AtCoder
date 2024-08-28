N, X = map(int, input().split())

sum = 0
for i in range(N):
    v, p = map(int, input().split())
    sum += p*v
    if sum > 100*X:
        print(i+1)
        exit()
        
print(-1)