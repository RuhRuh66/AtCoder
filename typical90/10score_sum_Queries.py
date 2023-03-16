N = int(input())

class1 = [0] * (N+1)
class2 = [0] * (N+1)

class1[0] = 0
class2[0] = 0

for i in range(1, N+1):
    c, p = map(int, input().split())
    if c == 1:
        class1[i] = class1[i-1] + p
        class2[i] = class2[i-1]
    else:
        class1[i] = class1[i-1] 
        class2[i] = class2[i-1] + p
    
    
Q = int(input())
for i in range(Q):
    L, R = map(int, input().split())
 
    print(class1[R]-class1[L-1], class2[R]-class2[L-1])

