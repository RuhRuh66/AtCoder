X = int(input())

ans = 0
for i in range(1,10**6):
    ans += i
    if X <= ans:
        break
print(i)



        
    