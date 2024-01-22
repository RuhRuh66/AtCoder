N = int(input())

A = list(map(int, input().split()))

B = set()
vet = 0
colors = ['gray', 'brown', 'green', 'lignt_blue', 'blue', 'yellow', 'orange', 'red', 'anonymus']
for i in range(N):
    temp = A[i] // 400
    if temp <= 7:
        B.add(colors[temp])
    else:
        vet += 1

if len(B) == 0:
    print(1, vet)
    exit()
        
min_ans = len(B)

max_ans = len(B) + vet


print(min_ans, max_ans)
         