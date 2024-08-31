N = int(input())

i = 1
cnt = 0
# ans = []
while i*i < 2*N:
    if 2*N % i == 0:
 
    
        j = 2*N//i
        if (i+j) % 2 == 1:
            cnt += 1
        # ans.append((i,j))

    i += 1
print(cnt*2)