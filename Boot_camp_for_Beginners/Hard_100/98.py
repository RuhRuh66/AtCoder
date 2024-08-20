H, W = map(int, input().split())

from collections import defaultdict

A = defaultdict(int)

for i in range(H):
    sts = list(input())
    for j in range(W):
        A[sts[j]] += 1




if H == 1 and W == 1:
    if len(A.items()) == 1:
        print('Yes')
        exit()
    else:
        print('No')
        exit()
if (H == 1 and W == 2) or (H==2 and W == 1):
    if  list(A.values())[0] == 2:
        print('Yes')
        exit()
    else:
        print('No')
        exit()

rm_4 = []
for k, v in A.items():
    v %= 4
    if v != 0:
        rm_4.append([k, v])

    
        
        
if H % 2 == 0 and W % 2 == 0:
    if len(rm_4) != 0:
        print('No')
    else:
        print('Yes')
elif H%2 == 0 and W%2 ==1:
    cnt = 0
    for k, v in rm_4:
        if v % 2== 1:
            print('No')
            exit()
        else:
            if v == 2:
                cnt += 2
    if cnt <= H:
        print('Yes')
    else:
        print('No')
elif H%2 == 1 and W%2 ==0:
    cnt = 0
    for k, v in rm_4:
        if v % 2== 1:
            print('No')
            exit()
            
        else:
            if v == 2:
                cnt += 2
    if cnt <= W:
        print('Yes')
    else:
        print('No')
else:
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    for k, v in rm_4:
        if v%2 ==0:
            cnt_2 += 2
        else:
            cnt_1 += 1
            cnt_3 += v
        
    if cnt_1 != 1:
        print('No')
    else:
        if cnt_2 + cnt_3 <= H+W-1:
            print('Yes')
        else:
            print('No')
            



    