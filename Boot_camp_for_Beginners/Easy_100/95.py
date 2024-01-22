A, B, C = sorted(list(map(int, input().split())))

count = 0

if (B-A)%2 == 0:
    count += (B-A)//2 + (C-B)
    
else:
    count += (B-A)//2+1 + (C+1-B)
    

print(count)