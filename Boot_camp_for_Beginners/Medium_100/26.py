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
        continue
    
print(count)