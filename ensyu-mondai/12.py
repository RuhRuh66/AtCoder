N = int(input())

flag = True
for i in range(2, (int(N**0.5)+1)):
    if N % i == 0:
        flag = False
        break
        
if flag:
    print('Yes')
else:
    print('No')