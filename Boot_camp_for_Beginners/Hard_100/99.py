N = int(input())
A = []
for i in range(N):
    a = int(input())
    A.append(a)

take_over = 0
count = 0

for i in range(N):
    q = (A[i] + take_over)//2
    take_over = min((A[i]+take_over) % 2, A[i])
    count += q
    
print(count)
    
    