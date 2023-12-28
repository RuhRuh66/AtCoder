N = int(input())

start = int(N**0.5)

ans = 0
for i in range(start):
    if N % (start-i) == 0:
        ans = start-i-1 + N//(start-i)-1
        break
    
print(ans)        
    
        