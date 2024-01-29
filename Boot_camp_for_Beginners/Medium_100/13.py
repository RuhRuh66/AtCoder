N = int(input())

now = [0, 0]
now_time = 0


for i in range(N):
    t, x, y = map(int, input().split())
    if (abs(x-now[0]) + abs(y-now[1]))>t-now_time:
        print('No')
        exit()
        
    else:
        if ((abs(x-now[0]) + abs(y-now[1])) % 2 == 1 and (t-now_time) % 2 == 0) or ((abs(x-now[0]) + abs(y-now[1])) % 2 == 0 and (t-now_time) % 2 == 1):
            print('No')
            exit()
            
        else:
            now = [x, y]
            now_time = t
            
print('Yes')