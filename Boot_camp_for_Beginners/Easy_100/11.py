N = int(input())

ans = 0
for i in range(1, 7):
    if 2**i <= N:
        ans = i
    else:
        break

print(2**ans)
        
