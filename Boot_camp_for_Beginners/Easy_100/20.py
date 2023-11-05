s = int(input())

A = []

A.append(s)

i = 1
Flag = True
while Flag:
    if A[i-1] %2 == 0:
       next_ele = A[i-1]//2    
    else:
        next_ele = A[i-1] *3 +1
    
    if next_ele not in A:
        A.append(next_ele)
        i += 1
    else:
        Flag = False

print(i+1)