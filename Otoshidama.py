N, Y = map(int, input().split())

flag = False

for a in range(N+1):
    if flag == True:
        break
    for b in range(N-a+1):
        c = (Y - 10000*a - 5000*b) // 1000
        if c >= 0 and a + b + c == N:
            flag = True
            print(a, b, c)
            
if flag == False:
    print(-1, -1, -1)