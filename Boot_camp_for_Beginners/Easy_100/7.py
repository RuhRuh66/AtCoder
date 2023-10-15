A = []
B = [[False] * 3 for i in range(3)]

for i in range(3):
    temp = list(map(int, input().split()))
    A.append(temp)
    
N = int(input())

for j in range(N):
    b = int(input())
    for k in range(3):
        for l in range(3):
            if A[k][l] == b:
                B[k][l] = True


flag = False
for m in range(3):
    if all(B[m]) == True:
        flag = True
        print('Yes')
        exit()
        
for n in range(3):
    if all([row[n] for row in B]):
        flag = True
        print('Yes')
        exit()

if all([B[o][o] for o in range(3)]):
    flag = True
    print('Yes')
    exit()
 
if all([B[2-o][o] for o in range(3)]):
    flag = True
    print('Yes')
    exit()
    
if flag == False:
    print('No')
   



    