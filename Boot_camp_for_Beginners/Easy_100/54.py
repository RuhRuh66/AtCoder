N = int(input())

w1 = list(str(input()))
en = w1[-1]
W = [w1]

flag  = True
for i in range(1, N):
    temp = list(str(input()))
    if temp in W:
        flag = False
        
    else:
        W.append(temp)
        st = temp[0]
        if st == en:
            en = temp[-1]
        else:
           flag = False

print('Yes' if flag else 'No')