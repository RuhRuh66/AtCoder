N = int(input())
A = list(map(int, input().split()))

def calc_or(left, right):
    result = 0
    for i in range(left, right):
        result = result | A[i]
    return result

ans = 2**40
for i in range(1<<(N-1)):
    septi = []
    for j in range(N-1):
        if i >> j  & 1 == 1:
            septi.append(j+1)
    septi = [0] + septi + [N]
    temp = 0
    for k in range(len(septi)-1):
        temp = calc_or(septi[k], septi[k+1]) ^ temp
    ans = min(ans, temp)
            
            
print(ans)

    
    
