R, G, B, N = map(int, input().split())

count = 0
for r in range(3001):
    if N-r*R <0:
        break
    for g in range(3001):
        if N-r*R-g*G < 0:
            break
        else:
            b = (N-r*R-g*G)/B
            if b.is_integer():
                count+=1
print(count)

