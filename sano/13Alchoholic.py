N, X = map(int, input().split())
alchohols = []
for i in range(N):
    temp = list(map(int, input().split()))
    alchohols.append(temp)
    
total = 0
count = 0
for i in alchohols:
    count += 1
    total += i[0] * i[1] 
    if total > 100 * X:
        print(count)
        exit()
        
print(-1)