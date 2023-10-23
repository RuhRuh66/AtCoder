N, A, B = map(int, input().split())
S = list(input())

total_num = A+B
foreign_num = B

for i in S:
    if i == 'c':
        print('No')
    elif i == 'a':
        if total_num > 0:
            print('Yes')
            total_num -= 1
        else:
            print('No')
            
    else:
        if total_num > 0 and foreign_num >0:
            print('Yes')
            total_num -= 1
            foreign_num -= 1
        else:
            print('No')