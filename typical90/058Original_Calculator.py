

n, k = map(int, input().split())
mod = 10 ** 5

nums = [-1] * 10**5

def calc(t):
    s = str(t)
    temp = 0
    for i in s:
        temp += int(i)
    u = (t + temp) % mod
    return(u)    

count = 0
v1 = n
nums[v1] = 0
for i in range(k):
    count += 1
    s = calc(v1)
    if nums[s] == -1:
        nums[s] = count
        v1 = s
        if count == k:
            print(s)
            exit()
    else:
        st = nums[s]
        cy = count-nums[s]
        k =((k-st) % cy) + st
        break
        

for i in range(k):
    n = calc(n)

print(n)
    



    