N, Y = map(int, input().split())

Y = Y//1000

for i in range(N+1):
    if i * 10 > Y:
        break
    for j in range(N-i+1):
        if i*10 + j*5 > Y:
            break
        else:
            if N-i-j < 0:
                break
            else:
                if i*10 + j*5 + (N-i-j) == Y:
                    print(i, j, N-i-j)
                    exit()
                    
print(' '.join(['-1','-1','-1'] ))