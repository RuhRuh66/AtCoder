N = int(input())

A = list(map(int, input().split()))

status = 'default'
count = 1

for i in range(1, N):
    if A[i] > A[i-1]:
        if status == 'up':
            continue
        elif status == 'down':
            count += 1
            status = 'default'
        else:
            status = 'up'
            
    elif A[i] < A[i-1]:
        if status == 'down':
            continue
        elif status == 'up':
            count += 1
            status = 'default'
        else:
            status = 'down'
            
    else:
<<<<<<< HEAD
        B.append('GT')

print(B)
        
for j in range(N-2):
    if B[j+1] == 'E' or B[j+1] == B[j]:
        continue
    else:
        B[j+1] = 'Sep'

print(B)
print(B.count('Sep') +1)
=======
        continue
    
print(count)
>>>>>>> ef1ef28138c258caa1ada7d679adb82f24a6df9f
