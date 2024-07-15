N, K = map(int, input().split())
S = str(input())

now = 1
cnt = 0

Nums = []

for i in range(N):
    if int(S[i]) == now:
        cnt += 1
    else:
        Nums.append(cnt)
        now = 1-now
        cnt = 1
        
if cnt != 0:
    Nums.append(cnt)
    
if len(Nums) % 2 == 0:
    Nums.append(0)
    
Add = 2*K + 1

ans = 0

right = 0
left = 0
temp = 0


for i in range(0, len(Nums), 2):
    Nextleft = i
    Nextright = min(i + Add, len(Nums))
    
    while Nextleft > left:
        temp -= Nums[left]
        left += 1
    while Nextright > right:
        temp += Nums[right]
        right += 1
        
    ans = max(temp, ans)

    
print(ans)
    

