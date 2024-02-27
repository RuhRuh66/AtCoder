N = int(input())
<<<<<<< HEAD
=======

>>>>>>> 0582d9815502e91159945ec2929bf1a1e3a479e7
H = list(map(int, input().split()))

active = 0
ans = 0

<<<<<<< HEAD
for i in range(N):
    if H[i] >= active:
        active = H[i]
        ans += H[i]-active

    else:
        ans += active-H[i]
        active = H[i]

print(ans)
=======

for i in range(N):
    if H[i] > active:
        active = H[i]
    elif H[i] == active:
        continue
    else:
        ans += active - H[i]
        active = H[i]
        
ans += active

print(ans) 
        
        
>>>>>>> 0582d9815502e91159945ec2929bf1a1e3a479e7
