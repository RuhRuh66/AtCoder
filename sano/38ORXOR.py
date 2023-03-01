N = int(input())
A = list(map(int, input().split()))

ans = 2**40

def calc_or(left, right):
    result = 0
    for i in range(left, right):
        result = result | A[i]
    
    return result

for i in range(1<<(N+1)):
    if i & 1 == 0 or i>>N & 1 == 0:
        continue
    
    partition = []
    for shift in range(N+1):
        if i >> shift & 1 == 1:
            partition.append(shift)
            
    ans_temp = 0
    for k in range(len(partition)-1):
        ans_temp = ans_temp^calc_or(partition[k], partition[k+1])
        
    ans = min(ans, ans_temp)
        
        
        
print(ans)