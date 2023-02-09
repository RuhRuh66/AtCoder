N = int(input())
time = [0]
co = [[0,0]]
for i in range(N):
    t, x, y = map(int, input().split())
    time.append(t)
    co.append([x, y])
    
flag = True
for i in range(N):
    time_usable = time[i+1] - time[i]
    dist = abs(co[i+1][0]-co[i][0]) + abs(co[i+1][1]-co[i][1])
    if time_usable < dist:
        flag = False
        break   
    else:
        if (time_usable - dist) % 2 == 1:
            flag = False
            break  
        else:
            flag = True

if flag == True:
    print('Yes')
else:
    print('No')